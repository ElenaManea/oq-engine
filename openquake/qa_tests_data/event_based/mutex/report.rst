Event Based QA Test, Case 1
===========================

+---------------+---------------------+
| checksum32    |1_700_332_127        |
+---------------+---------------------+
| date          |2021-05-02T09:25:49  |
+---------------+---------------------+
| engine_version|3.12.0-git9b6ffe086d |
+---------------+---------------------+

num_sites = 1, num_levels = 46, num_rlzs = 1

Parameters
----------
+--------------------------------+-------------------------------------------+
| calculation_mode               |'preclassical'                             |
+--------------------------------+-------------------------------------------+
| number_of_logic_tree_samples   |0                                          |
+--------------------------------+-------------------------------------------+
| maximum_distance               |{'default': [[1.0, 200.0], [10.0, 200.0]]} |
+--------------------------------+-------------------------------------------+
| investigation_time             |50.0                                       |
+--------------------------------+-------------------------------------------+
| ses_per_logic_tree_path        |2000                                       |
+--------------------------------+-------------------------------------------+
| truncation_level               |2.0                                        |
+--------------------------------+-------------------------------------------+
| rupture_mesh_spacing           |2.0                                        |
+--------------------------------+-------------------------------------------+
| complex_fault_mesh_spacing     |2.0                                        |
+--------------------------------+-------------------------------------------+
| width_of_mfd_bin               |1.0                                        |
+--------------------------------+-------------------------------------------+
| area_source_discretization     |20.0                                       |
+--------------------------------+-------------------------------------------+
| pointsource_distance           |None                                       |
+--------------------------------+-------------------------------------------+
| ground_motion_correlation_model|None                                       |
+--------------------------------+-------------------------------------------+
| minimum_intensity              |{}                                         |
+--------------------------------+-------------------------------------------+
| random_seed                    |42                                         |
+--------------------------------+-------------------------------------------+
| master_seed                    |123456789                                  |
+--------------------------------+-------------------------------------------+
| ses_seed                       |1066                                       |
+--------------------------------+-------------------------------------------+

Input files
-----------
+------------------------+-------------------------+
| Name                   |File                     |
+------------------------+-------------------------+
| gsim_logic_tree        |`gmmLT.xml <gmmLT.xml>`_ |
+------------------------+-------------------------+
| job_ini                |`job.ini <job.ini>`_     |
+------------------------+-------------------------+
| source_model_logic_tree|`ssmLT.xml <ssmLT.xml>`_ |
+------------------------+-------------------------+

Composite source model
----------------------
+-------+--------------------------+-----+
| grp_id|gsim                      |rlzs |
+-------+--------------------------+-----+
| 0     |'[SiMidorikawa1999SInter]'|[0]  |
+-------+--------------------------+-----+

Required parameters per tectonic region type
--------------------------------------------
+--------+--------------------------+---------+----------+---------------+
| trt_smr|gsims                     |distances|siteparams|ruptparams     |
+--------+--------------------------+---------+----------+---------------+
| 0      |'[SiMidorikawa1999SInter]'|rrup     |vs30      |hypo_depth mag |
+--------+--------------------------+---------+----------+---------------+

Slowest sources
---------------
+----------+----+---------+---------+-------------+
| source_id|code|calc_time|num_sites|eff_ruptures |
+----------+----+---------+---------+-------------+

Computation times by source typology
------------------------------------
+-----+---------+---------+-------------+
| code|calc_time|num_sites|eff_ruptures |
+-----+---------+---------+-------------+
| N   |0.0      |0        |0            |
+-----+---------+---------+-------------+

Information about the tasks
---------------------------
+-------------------+------+-------+------+-------+--------+
| operation-duration|counts|mean   |stddev|min    |max     |
+-------------------+------+-------+------+-------+--------+
| read_source_model |1     |0.38673|nan   |0.38673|0.38673 |
+-------------------+------+-------+------+-------+--------+

Data transfer
-------------
+------------------+----+----------+
| task             |sent|received  |
+------------------+----+----------+
| read_source_model|    |755.95 KB |
+------------------+----+----------+

Slowest operations
------------------
+-------------------------+--------+---------+-------+
| calc_3415, maxmem=0.3 GB|time_sec|memory_mb|counts |
+-------------------------+--------+---------+-------+
| composite source model  |0.97302 |1.98047  |1      |
+-------------------------+--------+---------+-------+
| total read_source_model |0.38673 |2.58984  |1      |
+-------------------------+--------+---------+-------+