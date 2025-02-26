Classical Hazard QA Test, Case 25, topographic surface1 (Mt Etna)
=================================================================

+---------------+---------------------+
| checksum32    |333_925_799          |
+---------------+---------------------+
| date          |2021-05-02T09:26:57  |
+---------------+---------------------+
| engine_version|3.12.0-git9b6ffe086d |
+---------------+---------------------+

num_sites = 6, num_levels = 3, num_rlzs = 1

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
| ses_per_logic_tree_path        |1                                          |
+--------------------------------+-------------------------------------------+
| truncation_level               |3.0                                        |
+--------------------------------+-------------------------------------------+
| rupture_mesh_spacing           |1.0                                        |
+--------------------------------+-------------------------------------------+
| complex_fault_mesh_spacing     |1.0                                        |
+--------------------------------+-------------------------------------------+
| width_of_mfd_bin               |0.1                                        |
+--------------------------------+-------------------------------------------+
| area_source_discretization     |1.0                                        |
+--------------------------------+-------------------------------------------+
| pointsource_distance           |None                                       |
+--------------------------------+-------------------------------------------+
| ground_motion_correlation_model|None                                       |
+--------------------------------+-------------------------------------------+
| minimum_intensity              |{}                                         |
+--------------------------------+-------------------------------------------+
| random_seed                    |23                                         |
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
| gsim_logic_tree        |`gmpe_logic_tree.xml <gmpe_logic_tree.xml>`_                 |
+------------------------+-------------------------------------------------------------+
| job_ini                |`job.ini <job.ini>`_                                         |
+------------------------+-------------------------------------------------------------+
| sites                  |`sites.csv <sites.csv>`_                                     |
+------------------------+-------------------------------------------------------------+
| source_model_logic_tree|`source_model_logic_tree.xml <source_model_logic_tree.xml>`_ |
+------------------------+-------------------------------------------------------------+

Composite source model
----------------------
+-------+-----------------------+-----+
| grp_id|gsim                   |rlzs |
+-------+-----------------------+-----+
| 0     |'[TusaLanger2016Rhypo]'|[0]  |
+-------+-----------------------+-----+

Required parameters per tectonic region type
--------------------------------------------
+--------+-----------------------+---------+----------+-----------+
| trt_smr|gsims                  |distances|siteparams|ruptparams |
+--------+-----------------------+---------+----------+-----------+
| 0      |'[TusaLanger2016Rhypo]'|rhypo    |vs30      |mag        |
+--------+-----------------------+---------+----------+-----------+

Slowest sources
---------------
+----------+----+---------+---------+-------------+
| source_id|code|calc_time|num_sites|eff_ruptures |
+----------+----+---------+---------+-------------+
| 1        |A   |0.02494  |6        |440          |
+----------+----+---------+---------+-------------+

Computation times by source typology
------------------------------------
+-----+---------+---------+-------------+
| code|calc_time|num_sites|eff_ruptures |
+-----+---------+---------+-------------+
| A   |0.02494  |6        |440          |
+-----+---------+---------+-------------+

Information about the tasks
---------------------------
+-------------------+------+-------+------+-------+--------+
| operation-duration|counts|mean   |stddev|min    |max     |
+-------------------+------+-------+------+-------+--------+
| preclassical      |1     |0.04125|nan   |0.04125|0.04125 |
+-------------------+------+-------+------+-------+--------+
| read_source_model |1     |0.00341|nan   |0.00341|0.00341 |
+-------------------+------+-------+------+-------+--------+

Data transfer
-------------
+------------------+----+---------+
| task             |sent|received |
+------------------+----+---------+
| read_source_model|    |1.72 KB  |
+------------------+----+---------+
| preclassical     |    |5.15 KB  |
+------------------+----+---------+

Slowest operations
------------------
+-------------------------+--------+---------+-------+
| calc_3462, maxmem=0.2 GB|time_sec|memory_mb|counts |
+-------------------------+--------+---------+-------+
| composite source model  |0.09690 |0.0      |1      |
+-------------------------+--------+---------+-------+
| total preclassical      |0.04125 |0.0      |1      |
+-------------------------+--------+---------+-------+
| splitting sources       |0.02525 |0.0      |1      |
+-------------------------+--------+---------+-------+
| weighting sources       |0.01544 |0.0      |1      |
+-------------------------+--------+---------+-------+
| total read_source_model |0.00341 |0.0      |1      |
+-------------------------+--------+---------+-------+