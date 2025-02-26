Classical Hazard Logic Tree with uncertainty in fault geometry and slip
=======================================================================

+---------------+---------------------+
| checksum32    |2_058_019_947        |
+---------------+---------------------+
| date          |2021-05-02T09:27:41  |
+---------------+---------------------+
| engine_version|3.12.0-git9b6ffe086d |
+---------------+---------------------+

num_sites = 1, num_levels = 6, num_rlzs = 4

Parameters
----------
+--------------------------------+-------------------------------------------+
| calculation_mode               |'preclassical'                             |
+--------------------------------+-------------------------------------------+
| number_of_logic_tree_samples   |0                                          |
+--------------------------------+-------------------------------------------+
| maximum_distance               |{'default': [[1.0, 400.0], [10.0, 400.0]]} |
+--------------------------------+-------------------------------------------+
| investigation_time             |1.0                                        |
+--------------------------------+-------------------------------------------+
| ses_per_logic_tree_path        |1                                          |
+--------------------------------+-------------------------------------------+
| truncation_level               |2.0                                        |
+--------------------------------+-------------------------------------------+
| rupture_mesh_spacing           |1.0                                        |
+--------------------------------+-------------------------------------------+
| complex_fault_mesh_spacing     |1.0                                        |
+--------------------------------+-------------------------------------------+
| width_of_mfd_bin               |0.25                                       |
+--------------------------------+-------------------------------------------+
| area_source_discretization     |None                                       |
+--------------------------------+-------------------------------------------+
| pointsource_distance           |None                                       |
+--------------------------------+-------------------------------------------+
| ground_motion_correlation_model|None                                       |
+--------------------------------+-------------------------------------------+
| minimum_intensity              |{}                                         |
+--------------------------------+-------------------------------------------+
| random_seed                    |1066                                       |
+--------------------------------+-------------------------------------------+
| master_seed                    |123456789                                  |
+--------------------------------+-------------------------------------------+
| ses_seed                       |42                                         |
+--------------------------------+-------------------------------------------+

Input files
-----------
+------------------------+-------------------------+
| Name                   |File                     |
+------------------------+-------------------------+
| gsim_logic_tree        |`gmcLT.xml <gmcLT.xml>`_ |
+------------------------+-------------------------+
| job_ini                |`job.ini <job.ini>`_     |
+------------------------+-------------------------+
| source_model_logic_tree|`sscLT.xml <sscLT.xml>`_ |
+------------------------+-------------------------+

Composite source model
----------------------
+-------+---------------------+-----+
| grp_id|gsim                 |rlzs |
+-------+---------------------+-----+
| 0     |'[BooreAtkinson2008]'|[0]  |
+-------+---------------------+-----+
| 1     |'[BooreAtkinson2008]'|[1]  |
+-------+---------------------+-----+
| 2     |'[BooreAtkinson2008]'|[2]  |
+-------+---------------------+-----+
| 3     |'[BooreAtkinson2008]'|[3]  |
+-------+---------------------+-----+

Required parameters per tectonic region type
--------------------------------------------
+--------+---------------------+---------+----------+-----------+
| trt_smr|gsims                |distances|siteparams|ruptparams |
+--------+---------------------+---------+----------+-----------+
| 0      |'[BooreAtkinson2008]'|rjb      |vs30      |mag rake   |
+--------+---------------------+---------+----------+-----------+
| 1      |'[BooreAtkinson2008]'|rjb      |vs30      |mag rake   |
+--------+---------------------+---------+----------+-----------+
| 2      |'[BooreAtkinson2008]'|rjb      |vs30      |mag rake   |
+--------+---------------------+---------+----------+-----------+
| 3      |'[BooreAtkinson2008]'|rjb      |vs30      |mag rake   |
+--------+---------------------+---------+----------+-----------+

Slowest sources
---------------
+----------+----+---------+---------+-------------+
| source_id|code|calc_time|num_sites|eff_ruptures |
+----------+----+---------+---------+-------------+
| src1;1   |S   |0.08993  |1        |714          |
+----------+----+---------+---------+-------------+
| src1;0   |S   |0.08267  |1        |714          |
+----------+----+---------+---------+-------------+
| src1;2   |S   |0.07957  |1        |357          |
+----------+----+---------+---------+-------------+
| src1;3   |S   |0.07104  |1        |357          |
+----------+----+---------+---------+-------------+

Computation times by source typology
------------------------------------
+-----+---------+---------+-------------+
| code|calc_time|num_sites|eff_ruptures |
+-----+---------+---------+-------------+
| S   |0.32322  |4        |2_142        |
+-----+---------+---------+-------------+

Information about the tasks
---------------------------
+-------------------+------+-------+------+-------+--------+
| operation-duration|counts|mean   |stddev|min    |max     |
+-------------------+------+-------+------+-------+--------+
| preclassical      |4     |0.11269|6%    |0.10602|0.12365 |
+-------------------+------+-------+------+-------+--------+
| read_source_model |1     |0.00213|nan   |0.00213|0.00213 |
+-------------------+------+-------+------+-------+--------+

Data transfer
-------------
+------------------+---------------------------------------------+---------+
| task             |sent                                         |received |
+------------------+---------------------------------------------+---------+
| read_source_model|                                             |1.48 KB  |
+------------------+---------------------------------------------+---------+
| preclassical     |srcs=5.11 KB srcfilter=2.86 KB params=1.48 KB|6.2 KB   |
+------------------+---------------------------------------------+---------+

Slowest operations
------------------
+-------------------------+--------+---------+-------+
| calc_3483, maxmem=0.7 GB|time_sec|memory_mb|counts |
+-------------------------+--------+---------+-------+
| total preclassical      |0.45076 |1.22266  |4      |
+-------------------------+--------+---------+-------+
| splitting sources       |0.32450 |1.04688  |4      |
+-------------------------+--------+---------+-------+
| composite source model  |0.24957 |0.0      |1      |
+-------------------------+--------+---------+-------+
| weighting sources       |0.12324 |0.25000  |4      |
+-------------------------+--------+---------+-------+
| total read_source_model |0.00213 |0.0      |1      |
+-------------------------+--------+---------+-------+