# -*- coding: utf-8 -*-
# vim: tabstop=4 shiftwidth=4 softtabstop=4
#
# Copyright (c) 2016-2021 GEM Foundation
#
# OpenQuake is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# OpenQuake is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with OpenQuake.  If not, see <http://www.gnu.org/licenses/>.
from openquake.baselib.python3compat import zip
from openquake.baselib.performance import numba, compile
import numpy

F32 = numpy.float32
F64 = numpy.float64
BYTES_PER_FLOAT = 8

if numba:
    @compile("void(float64[:, :], float64[:], uint32[:])")
    def combine_probs(array, other, rlzs):
        for li in range(len(array)):
            for ri in rlzs:
                if other[li] != 0.:
                    array[li, ri] = (
                        1. - (1. - array[li, ri]) * (1. - other[li]))
else:
    def combine_probs(array, other, rlzs):
        for r in rlzs:
            array[:, r] = (1. - (1. - array[:, r]) * (1. - other))


class AllEmptyProbabilityMaps(ValueError):
    """
    Raised by get_shape(pmaps) if all passed probability maps are empty
    """


class ProbabilityCurve(object):
    """
    This class is a small wrapper over an array of PoEs associated to
    a set of intensity measure types and levels. It provides a few operators,
    including the complement operator `~`

    ~p = 1 - p

    and the inclusive or operator `|`

    p = p1 | p2 = ~(~p1 * ~p2)

    Such operators are implemented efficiently at the numpy level, by
    dispatching on the underlying array.

    Here is an example of use:

    >>> poe = ProbabilityCurve(numpy.array([0.1, 0.2, 0.3, 0, 0]))
    >>> ~(poe | poe) * .5
    <ProbabilityCurve
    [0.405 0.32  0.245 0.5   0.5  ]>
    """
    def __init__(self, array):
        self.array = array

    def __or__(self, other):
        if other == 0:
            return self
        else:
            return self.__class__(1. - (1. - self.array) * (1. - other.array))
    __ror__ = __or__

    def __iadd__(self, other):
        # this is used when composing mutually exclusive probabilities
        self.array += other.array
        return self

    def __add__(self, other):
        # this is used when composing mutually exclusive probabilities
        self.array += other.array
        return self.__class__(self.array)

    def __mul__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(self.array * other.array)
        elif other == 1:
            return self
        else:
            return self.__class__(self.array * other)
    __rmul__ = __mul__

    def __pow__(self, n):
        return self.__class__(self.array ** n)

    def __invert__(self):
        return self.__class__(1. - self.array)

    def __bool__(self):
        return bool(self.array.any())

    def __repr__(self):
        return '<ProbabilityCurve\n%s>' % self.array

    def extract(self, inner_idx):
        """
        Extracts the component specified by the index `inner_idx`.
        """
        array = self.array[:, inner_idx].reshape(-1, 1)
        return self.__class__(array)

    def combine(self, other, rlz_groups):
        """
        Update a ProbabilityCurve with shape (L, R) with a pcurve with shape
        (L, G), being G the number of realization groups, which are list
        of integers in the range 0..R-1.
        """
        for g, rlz_group in enumerate(rlz_groups):
            combine_probs(self.array, other.array[:, g], rlz_group)

    # used when exporting to HDF5
    def convert(self, imtls, idx=0):
        """
        Convert a probability curve into a record of dtype `imtls.dt`.

        :param imtls: DictArray instance
        :param idx: extract the data corresponding to the given inner index
        """
        curve = numpy.zeros(1, imtls.dt)
        for imt in imtls:
            curve[imt] = self.array[imtls(imt), idx]
        return curve[0]


class ProbabilityMap(dict):
    """
    A dictionary site_id -> ProbabilityCurve. It defines the complement
    operator `~`, performing the complement on each curve

    ~p = 1 - p

    and the "inclusive or" operator `|`:

    m = m1 | m2 = {sid: m1[sid] | m2[sid] for sid in all_sids}

    Such operators are implemented efficiently at the numpy level, by
    dispatching on the underlying array. Moreover there is a classmethod
    .build(L, I, sids, initvalue) to build initialized instances of
    :class:`ProbabilityMap`. The map can be represented as 3D array of shape
    (shape_x, shape_y, shape_z) = (N, L, I), where N is the number of site IDs,
    L the total number of hazard levels and I the number of GSIMs.
    """
    @classmethod
    def build(cls, shape_y, shape_z, sids=(), initvalue=0., dtype=F64):
        """
        :param shape_y: the total number of intensity measure levels
        :param shape_z: the number of inner levels
        :param sids: a set of site indices
        :param initvalue: the initial value of the probability (default 0)
        :returns: a ProbabilityMap dictionary
        """
        dic = cls(shape_y, shape_z)
        for sid in sids:
            dic.setdefault(sid, initvalue, dtype)
        return dic

    @classmethod
    def from_array(cls, array, sids):
        """
        :param array: array of shape (N, L) or (N, L, I)
        :param sids: array of N site IDs
        """
        n_sites = len(sids)
        n = len(array)
        if n_sites != n:
            raise ValueError('Passed %d site IDs, but the array has length %d'
                             % (n_sites, n))
        if len(array.shape) == 2:  # shape (N, L) -> (N, L, 1)
            array = array.reshape(array.shape + (1,))
        self = cls(*array.shape[1:])
        for sid, poes in zip(sids, array):
            self[sid] = ProbabilityCurve(poes)
        return self

    def __init__(self, shape_y, shape_z=1):
        self.shape_y = shape_y
        self.shape_z = shape_z

    def setdefault(self, sid, value, dtype=F64):
        """
        Works like `dict.setdefault`: if the `sid` key is missing, it fills
        it with an array and returns the associate ProbabilityCurve

        :param sid: site ID
        :param value: value used to fill the returned ProbabilityCurve
        :param dtype: dtype used internally (F32 or F64)
        """
        try:
            return self[sid]
        except KeyError:
            array = numpy.empty((self.shape_y, self.shape_z), dtype)
            array.fill(value)
            pc = ProbabilityCurve(array)
            self[sid] = pc
            return pc

    @property
    def sids(self):
        """The ordered keys of the map as a numpy.uint32 array"""
        return numpy.array(sorted(self), numpy.uint32)

    def array(self, start, stop, g):
        """
        An array of shape (stop-start, L)
        """
        arr = numpy.zeros((stop-start, self.shape_y))
        for i, sid in enumerate(range(start, stop)):
            try:
                arr[i] = self[sid].array[:, g]
            except KeyError:
                pass
        # Physically, an extremely small intensity measure level can have an
        # extremely large probability of exceedence, however that probability
        # cannot be exactly 1 unless the level is exactly 0. Numerically, the
        # PoE can be 1 and this give issues when calculating the damage (there
        # is a log(0) in
        # :class:`openquake.risklib.scientific.annual_frequency_of_exceedence`).
        # Here we solve the issue by replacing the unphysical probabilities 1
        # with .9999999999999999 (the float64 closest to 1).
        arr[arr == 1.] = .9999999999999999
        return arr

    @property
    def nbytes(self):
        """The size of the underlying array"""
        try:
            N, L, I = get_shape([self])
        except AllEmptyProbabilityMaps:
            return 0
        return BYTES_PER_FLOAT * N * L * I

    # used when exporting to HDF5
    def convert(self, imtls, nsites, idx=0):
        """
        Convert a probability map into a composite array of length `nsites`
        and dtype `imtls.dt`.

        :param imtls:
            DictArray instance
        :param nsites:
            the total number of sites
        :param idx:
            index on the z-axis (default 0)
        """
        curves = numpy.zeros(nsites, imtls.dt)
        for imt in curves.dtype.names:
            curves_by_imt = curves[imt]
            for sid in self:
                curves_by_imt[sid] = self[sid].array[imtls(imt), idx]
        return curves

    def filter(self, sids):
        """
        Extracs a submap of self for the given sids.
        """
        dic = self.__class__(self.shape_y, self.shape_z)
        for sid in sids:
            try:
                dic[sid] = self[sid]
            except KeyError:
                pass
        return dic

    def extract(self, inner_idx):
        """
        Extracts a component of the underlying ProbabilityCurves,
        specified by the index `inner_idx`.
        """
        out = self.__class__(self.shape_y, 1)
        for sid in self:
            curve = self[sid]
            array = curve.array[:, inner_idx].reshape(-1, 1)
            out[sid] = ProbabilityCurve(array)
        return out

    def combine(self, pmap, rlz_groups):
        """
        Update a ProbabilityMap with shape (L, R) with a pmap with shape
        (L, G), being G the number of realization groups, which are list
        of integers in the range 0..R-1.
        """
        for sid in pmap:
            self[sid].combine(pmap[sid], rlz_groups)

    def __ior__(self, other):
        if not other:
            return self
        if (other.shape_y, other.shape_z) != (self.shape_y, self.shape_z):
            raise ValueError('%s has inconsistent shape with %s' %
                             (other, self))
        self_sids = set(self)
        other_sids = set(other)
        for sid in self_sids & other_sids:
            self[sid] = self[sid] | other[sid]
        for sid in other_sids - self_sids:
            self[sid] = other[sid]
        return self

    def __or__(self, other):
        new = self.__class__(self.shape_y, self.shape_z)
        new.update(self)
        new |= other
        return new

    __ror__ = __or__

    def __add__(self, other):
        try:
            other.get
            is_pmap = True
            sids = set(self) | set(other)
        except AttributeError:  # no .get method, assume a float
            is_pmap = False
            assert 0. <= other <= 1., other  # must be a probability
            sids = set(self)
        new = self.__class__(self.shape_y, self.shape_z)
        for sid in sids:
            prob = other.get(sid, 1) if is_pmap else other
            new[sid] = self.get(sid, 1) + prob
        return new

    def __iadd__(self, other):
        # this is used when composing mutually exclusive probabilities
        for sid in other:
            pcurve = self.setdefault(sid, 0)
            pcurve += other[sid]
        return self

    def __mul__(self, other):
        try:
            other.get
            is_pmap = True
            sids = set(self) | set(other)
        except AttributeError:  # no .get method, assume a float
            is_pmap = False
            assert 0. <= other <= 1., other  # must be a probability
            sids = set(self)
        new = self.__class__(self.shape_y, self.shape_z)
        for sid in sids:
            prob = other.get(sid, 1) if is_pmap else other
            new[sid] = self.get(sid, 1) * prob
        return new

    def __ipow__(self, n):
        for sid, pcurve in self.items():
            self[sid] = pcurve ** n
        return self

    def __pow__(self, n):
        new = self.__class__(self.shape_y, self.shape_z)
        for sid, pcurve in self.items():
            new[sid] = pcurve ** n
        return new

    def __invert__(self):
        new = self.__class__(self.shape_y, self.shape_z)
        for sid in self:
            if (self[sid].array != 1.).any():
                new[sid] = ~self[sid]  # store only nonzero probabilities
        return new

    def __getstate__(self):
        return dict(shape_y=self.shape_y, shape_z=self.shape_z)


def get_shape(pmaps):
    """
    :param pmaps: a set of homogenous ProbabilityMaps
    :returns: the common shape (N, L, I)
    """
    for pmap in pmaps:
        if pmap:
            sid = next(iter(pmap))
            break
    else:
        raise AllEmptyProbabilityMaps(pmaps)
    return (len(pmap),) + pmap[sid].array.shape


def combine(pmaps):
    """
    :param pmaps: a set of homogenous ProbabilityMaps
    :returns: the combined map
    """
    shape = get_shape(pmaps)
    res = ProbabilityMap(shape[1], shape[2])
    for pmap in pmaps:
        res |= pmap
    return res
