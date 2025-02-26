# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4
#
# Copyright (C) 2010-2021 GEM Foundation
#
# OpenQuake is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# OpenQuake is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with OpenQuake. If not, see <http://www.gnu.org/licenses/>.
"""
Set up some system-wide loggers
"""
import os
import re
import socket
import getpass
import logging
import traceback
from datetime import datetime
from openquake.baselib import config, zeromq, parallel
from openquake.commonlib import readinput

LEVELS = {'debug': logging.DEBUG,
          'info': logging.INFO,
          'warn': logging.WARNING,
          'error': logging.ERROR,
          'critical': logging.CRITICAL}
CALC_REGEX = r'(calc|cache)_(\d+)\.hdf5'
DBSERVER_PORT = int(os.environ.get('OQ_DBSERVER_PORT') or config.dbserver.port)


def dbcmd(action, *args):
    """
    A dispatcher to the database server.

    :param string action: database action to perform
    :param tuple args: arguments
    """
    host = socket.gethostbyname(config.dbserver.host)
    sock = zeromq.Socket(
        'tcp://%s:%s' % (host, DBSERVER_PORT), zeromq.zmq.REQ, 'connect')
    with sock:
        res = sock.send((action,) + args)
        if isinstance(res, parallel.Result):
            return res.get()
    return res


def get_datadir():
    """
    Extracts the path of the directory where the openquake data are stored
    from the environment ($OQ_DATADIR) or from the shared_dir in the
    configuration file.
    """
    datadir = os.environ.get('OQ_DATADIR')
    if not datadir:
        shared_dir = config.directory.shared_dir
        if shared_dir:
            datadir = os.path.join(shared_dir, getpass.getuser(), 'oqdata')
        else:  # use the home of the user
            datadir = os.path.join(os.path.expanduser('~'), 'oqdata')
    return datadir


def get_calc_ids(datadir=None):
    """
    Extract the available calculation IDs from the datadir, in order.
    """
    datadir = datadir or get_datadir()
    if not os.path.exists(datadir):
        return []
    calc_ids = set()
    for f in os.listdir(datadir):
        mo = re.match(CALC_REGEX, f)
        if mo:
            calc_ids.add(int(mo.group(2)))
    return sorted(calc_ids)


def get_last_calc_id(datadir=None):
    """
    Extract the latest calculation ID from the given directory.
    If none is found, return 0.
    """
    datadir = datadir or get_datadir()
    calcs = get_calc_ids(datadir)
    if not calcs:
        return 0
    return calcs[-1]


def _update_log_record(self, record):
    """
    Massage a log record before emitting it. Intended to be used by the
    custom log handlers defined in this module.
    """
    if not hasattr(record, 'hostname'):
        record.hostname = '-'
    if not hasattr(record, 'job_id'):
        record.job_id = self.job_id


class LogStreamHandler(logging.StreamHandler):
    """
    Log stream handler
    """
    def __init__(self, job_id):
        super().__init__()
        self.job_id = job_id

    def emit(self, record):  # pylint: disable=E0202
        _update_log_record(self, record)
        super().emit(record)


class LogFileHandler(logging.FileHandler):
    """
    Log file handler
    """
    def __init__(self, job_id, log_file):
        super().__init__(log_file)
        self.job_id = job_id
        self.log_file = log_file

    def emit(self, record):  # pylint: disable=E0202
        _update_log_record(self, record)
        super().emit(record)


class LogDatabaseHandler(logging.Handler):
    """
    Log stream handler
    """
    def __init__(self, job_id):
        super().__init__()
        self.job_id = job_id

    def emit(self, record):  # pylint: disable=E0202
        if record.levelno >= logging.INFO:
            dbcmd('log', self.job_id, datetime.utcnow(), record.levelname,
                  '%s/%s' % (record.processName, record.process),
                  record.getMessage())


class LogContext:
    """
    Context manager managing the logging functionality
    """
    multi = False

    def __init__(self, job_ini, job=True, log_level='info', log_file=None,
                 user_name=None, hc_id=None):
        self.job = job
        self.log_level = log_level
        self.log_file = log_file
        self.user_name = user_name
        if isinstance(job_ini, dict):  # dictionary of parameters
            self.params = job_ini
        else:  # path to job.ini file
            self.params = readinput.get_params(job_ini)
        self.params['hazard_calculation_id'] = hc_id
        if job:
            self.calc_id = dbcmd(
                'create_job',
                get_datadir(),
                self.params['calculation_mode'],
                self.params['description'],
                user_name,
                hc_id)
        else:
            # only works in single-user situations
            self.calc_id = get_last_calc_id() + 1

    def get_oqparam(self):
        """
        :returns: a validated OqParam instance
        """
        return readinput.get_oqparam(self.params)

    def __enter__(self):
        if not logging.root.handlers:  # first time
            level = LEVELS.get(self.log_level, self.log_level)
            logging.basicConfig(level=level)
        f = '[%(asctime)s #{} %(levelname)s] %(message)s'.format(self.calc_id)
        for handler in logging.root.handlers:
            fmt = logging.Formatter(f, datefmt='%Y-%m-%d %H:%M:%S')
            handler.setFormatter(fmt)
        self.handlers = []
        if self.job:
            self.handlers.append(LogDatabaseHandler(self.calc_id))
        if self.log_file is None:
            # add a StreamHandler if not already there
            if not any(h for h in logging.root.handlers
                       if isinstance(h, logging.StreamHandler)):
                self.handlers.append(LogStreamHandler(self.calc_id))
        else:
            self.handlers.append(LogFileHandler(self.calc_id, self.log_file))
        for handler in self.handlers:
            logging.root.addHandler(handler)
        return self

    def __exit__(self, etype, exc, tb):
        if self.job:
            if tb:
                logging.critical(traceback.format_exc())
                dbcmd('finish', self.calc_id, 'failed')
            else:
                dbcmd('finish', self.calc_id, 'complete')
        for handler in self.handlers:
            logging.root.removeHandler(handler)
        parallel.Starmap.shutdown()

    def __getstate__(self):
        # ensure pickleability
        return dict(calc_id=self.calc_id, job=self.job, params=self.params,
                    log_level=self.log_level, log_file=self.log_file,
                    user_name=self.user_name)

    def __repr__(self):
        hc_id = self.params.get('hazard_calculation_id')
        return '<%s#%d, hc_id=%s>' % (self.__class__.__name__,
                                      self.calc_id, hc_id)


def init(job_or_calc, job_ini, log_level='info', log_file=None,
         user_name=None, hc_id=None):
    """
    :param job_or_calc: the string "job" or "calc"
    :param job_ini: path to the job.ini file or dictionary of parameters
    :param log_level: the log level as a string or number
    :param log_file: path to the log file (if any)
    :param user_name: user running the job (None means current user)
    :param hc_id: parent calculation ID (default None)
    :returns: a LogContext instance

    1. initialize the root logger (if not already initialized)
    2. set the format of the root log handlers (if any)
    3. create a job in the database if job_or_calc == "job"
    4. return a LogContext instance associated to a calculation ID
    """
    assert job_or_calc in {"job", "calc"}, job_or_calc
    return LogContext(job_ini, job_or_calc == "job",
                      log_level, log_file, user_name, hc_id)
