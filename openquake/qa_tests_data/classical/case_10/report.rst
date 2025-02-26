Classical Hazard QA Test, Case 10
=================================

+---------------+---------------------+
| checksum32    |2_930_421_535        |
+---------------+---------------------+
| date          |2021-05-02T09:26:18  |
+---------------+---------------------+
| engine_version|3.12.0-git9b6ffe086d |
+---------------+---------------------+

num_sites = 1, num_levels = 4, num_rlzs = 2

Parameters
----------
+--------------------------------+-------------------------------------------+
| calculation_mode               |'preclassical'                             |
+--------------------------------+-------------------------------------------+
| number_of_logic_tree_samples   |0                                          |
+--------------------------------+-------------------------------------------+
| maximum_distance               |{'default': [[1.0, 200.0], [10.0, 200.0]]} |
+--------------------------------+-------------------------------------------+
| investigation_time             |1.0                                        |
+--------------------------------+-------------------------------------------+
| ses_per_logic_tree_path        |1                                          |
+--------------------------------+-------------------------------------------+
| truncation_level               |0.0                                        |
+--------------------------------+-------------------------------------------+
| rupture_mesh_spacing           |0.01                                       |
+--------------------------------+-------------------------------------------+
| complex_fault_mesh_spacing     |0.01                                       |
+--------------------------------+-------------------------------------------+
| width_of_mfd_bin               |0.001                                      |
+--------------------------------+-------------------------------------------+
| area_source_discretization     |10.0                                       |
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
+------------------------+-------------------------------------------------------------+
| Name                   |File                                                         |
+------------------------+-------------------------------------------------------------+
| gsim_logic_tree        |`gsim_logic_tree.xml <gsim_logic_tree.xml>`_                 |
+------------------------+-------------------------------------------------------------+
| job_ini                |`job.ini <job.ini>`_                                         |
+------------------------+-------------------------------------------------------------+
| source_model_logic_tree|`source_model_logic_tree.xml <source_model_logic_tree.xml>`_ |
+------------------------+-------------------------------------------------------------+

Composite source model
----------------------
+-------+------------------+-----+
| grp_id|gsim              |rlzs |
+-------+------------------+-----+
| 0     |'[SadighEtAl1997]'|[0]  |
+-------+------------------+-----+
| 1     |'[SadighEtAl1997]'|[1]  |
+-------+------------------+-----+

Required parameters per tectonic region type
--------------------------------------------
+--------+------------------+---------+----------+-----------+
| trt_smr|gsims             |distances|siteparams|ruptparams |
+--------+------------------+---------+----------+-----------+
| 0      |'[SadighEtAl1997]'|rrup     |vs30      |mag rake   |
+--------+------------------+---------+----------+-----------+
| 1      |'[SadighEtAl1997]'|rrup     |vs30      |mag rake   |
+--------+------------------+---------+----------+-----------+

Slowest sources
---------------
+----------+----+---------+---------+-------------+
| source_id|code|calc_time|num_sites|eff_ruptures |
+----------+----+---------+---------+-------------+
| 1;0      |P   |0.00637  |1        |3_000        |
+----------+----+---------+---------+-------------+
| 1;1      |P   |0.00609  |1        |3_000        |
+----------+----+---------+---------+-------------+

Computation times by source typology
------------------------------------
+-----+---------+---------+-------------+
| code|calc_time|num_sites|eff_ruptures |
+-----+---------+---------+-------------+
| P   |0.01247  |2        |6_000        |
+-----+---------+---------+-------------+

Information about the tasks
---------------------------
+-------------------+------+-------+------+-------+--------+
| operation-duration|counts|mean   |stddev|min    |max     |
+-------------------+------+-------+------+-------+--------+
| preclassical      |2     |0.00983|2%    |0.00963|0.01003 |
+-------------------+------+-------+------+-------+--------+
| read_source_model |1     |0.00188|nan   |0.00188|0.00188 |
+-------------------+------+-------+------+-------+--------+

Data transfer
-------------
+------------------+-----------------------------------------------+---------+
| task             |sent                                           |received |
+------------------+-----------------------------------------------+---------+
| read_source_model|                                               |1.46 KB  |
+------------------+-----------------------------------------------+---------+
| preclassical     |srcfilter=16.71 KB params=15.94 KB srcs=2.19 KB|2.92 KB  |
+------------------+-----------------------------------------------+---------+

Slowest operations
------------------
+-------------------------+--------+---------+-------+
| calc_3438, maxmem=0.6 GB|time_sec|memory_mb|counts |
+-------------------------+--------+---------+-------+
| composite source model  |0.13497 |0.0      |1      |
+-------------------------+--------+---------+-------+
| total preclassical      |0.01966 |0.87109  |2      |
+-------------------------+--------+---------+-------+
| splitting sources       |0.01295 |0.80859  |2      |
+-------------------------+--------+---------+-------+
| weighting sources       |0.00585 |0.06250  |2      |
+-------------------------+--------+---------+-------+
| total read_source_model |0.00188 |0.0      |1      |
+-------------------------+--------+---------+-------+