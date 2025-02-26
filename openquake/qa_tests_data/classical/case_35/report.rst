Classical Hazard QA Test, Case 35 - Cluster model
=================================================

+---------------+---------------------+
| checksum32    |419_895_093          |
+---------------+---------------------+
| date          |2021-05-02T09:27:39  |
+---------------+---------------------+
| engine_version|3.12.0-git9b6ffe086d |
+---------------+---------------------+

num_sites = 1, num_levels = 5, num_rlzs = 1

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
| truncation_level               |10.0                                       |
+--------------------------------+-------------------------------------------+
| rupture_mesh_spacing           |10.0                                       |
+--------------------------------+-------------------------------------------+
| complex_fault_mesh_spacing     |10.0                                       |
+--------------------------------+-------------------------------------------+
| width_of_mfd_bin               |1.0                                        |
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

Required parameters per tectonic region type
--------------------------------------------
+--------+------------------+---------+----------+-----------+
| trt_smr|gsims             |distances|siteparams|ruptparams |
+--------+------------------+---------+----------+-----------+
| 0      |'[SadighEtAl1997]'|rrup     |vs30      |mag rake   |
+--------+------------------+---------+----------+-----------+

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
| X   |0.0      |0        |0            |
+-----+---------+---------+-------------+

Information about the tasks
---------------------------
+-------------------+------+-------+------+-------+--------+
| operation-duration|counts|mean   |stddev|min    |max     |
+-------------------+------+-------+------+-------+--------+
| read_source_model |1     |0.01029|nan   |0.01029|0.01029 |
+-------------------+------+-------+------+-------+--------+

Data transfer
-------------
+------------------+----+---------+
| task             |sent|received |
+------------------+----+---------+
| read_source_model|    |3.49 KB  |
+------------------+----+---------+

Slowest operations
------------------
+-------------------------+--------+---------+-------+
| calc_3480, maxmem=0.2 GB|time_sec|memory_mb|counts |
+-------------------------+--------+---------+-------+
| composite source model  |0.09541 |0.0      |1      |
+-------------------------+--------+---------+-------+
| total read_source_model |0.01029 |0.0      |1      |
+-------------------------+--------+---------+-------+