British Columbia With Vs30
==========================

+---------------+---------------------+
| checksum32    |857_888_332          |
+---------------+---------------------+
| date          |2021-05-02T09:25:31  |
+---------------+---------------------+
| engine_version|3.12.0-git9b6ffe086d |
+---------------+---------------------+

num_sites = 2, num_levels = 3, num_rlzs = 15

Parameters
----------
+--------------------------------+---------------------------------------------------------------------------------------------+
| calculation_mode               |'preclassical'                                                                               |
+--------------------------------+---------------------------------------------------------------------------------------------+
| number_of_logic_tree_samples   |0                                                                                            |
+--------------------------------+---------------------------------------------------------------------------------------------+
| maximum_distance               |{'default': [[1.0, 800], [10.0, 800]], 'Active Shallow Offshore': [[1.0, 800], [10.0, 800]]} |
+--------------------------------+---------------------------------------------------------------------------------------------+
| investigation_time             |20.0                                                                                         |
+--------------------------------+---------------------------------------------------------------------------------------------+
| ses_per_logic_tree_path        |1                                                                                            |
+--------------------------------+---------------------------------------------------------------------------------------------+
| truncation_level               |3.0                                                                                          |
+--------------------------------+---------------------------------------------------------------------------------------------+
| rupture_mesh_spacing           |5.0                                                                                          |
+--------------------------------+---------------------------------------------------------------------------------------------+
| complex_fault_mesh_spacing     |10.0                                                                                         |
+--------------------------------+---------------------------------------------------------------------------------------------+
| width_of_mfd_bin               |0.1                                                                                          |
+--------------------------------+---------------------------------------------------------------------------------------------+
| area_source_discretization     |15.0                                                                                         |
+--------------------------------+---------------------------------------------------------------------------------------------+
| pointsource_distance           |None                                                                                         |
+--------------------------------+---------------------------------------------------------------------------------------------+
| ground_motion_correlation_model|None                                                                                         |
+--------------------------------+---------------------------------------------------------------------------------------------+
| minimum_intensity              |{'default': 0.001, 'SA(0.3)': 0.001, 'SA(0.6)': 0.001, 'SA(1.0)': 0.001}                     |
+--------------------------------+---------------------------------------------------------------------------------------------+
| random_seed                    |24                                                                                           |
+--------------------------------+---------------------------------------------------------------------------------------------+
| master_seed                    |123456789                                                                                    |
+--------------------------------+---------------------------------------------------------------------------------------------+
| ses_seed                       |23                                                                                           |
+--------------------------------+---------------------------------------------------------------------------------------------+

Input files
-----------
+------------------------+------------------------------------------------------+
| Name                   |File                                                  |
+------------------------+------------------------------------------------------+
| exposure               |`BC_Exposure.xml <BC_Exposure.xml>`_                  |
+------------------------+------------------------------------------------------+
| gsim_logic_tree        |`gmmLT_analytical.xml <gmmLT_analytical.xml>`_        |
+------------------------+------------------------------------------------------+
| job_ini                |`job.ini <job.ini>`_                                  |
+------------------------+------------------------------------------------------+
| site_model             |`vs30_a.xml <vs30_a.xml>`_ `vs30_b.xml <vs30_b.xml>`_ |
+------------------------+------------------------------------------------------+
| source_model_logic_tree|`ssmLT.xml <ssmLT.xml>`_                              |
+------------------------+------------------------------------------------------+

Composite source model
----------------------
+-------+--------------------------------------------------+-----------+
| grp_id|gsim                                              |rlzs       |
+-------+--------------------------------------------------+-----------+
| 0     |"[NRCan15SiteTerm]\ngmpe_name = 'OceanicCan15Low'"|[0, 6, 9]  |
+-------+--------------------------------------------------+-----------+
| 0     |"[NRCan15SiteTerm]\ngmpe_name = 'OceanicCan15Mid'"|[1, 7, 10] |
+-------+--------------------------------------------------+-----------+
| 0     |"[NRCan15SiteTerm]\ngmpe_name = 'OceanicCan15Upp'"|[2, 8, 11] |
+-------+--------------------------------------------------+-----------+
| 1     |"[NRCan15SiteTerm]\ngmpe_name = 'OceanicCan15Low'"|[3, 12]    |
+-------+--------------------------------------------------+-----------+
| 1     |"[NRCan15SiteTerm]\ngmpe_name = 'OceanicCan15Mid'"|[4, 13]    |
+-------+--------------------------------------------------+-----------+
| 1     |"[NRCan15SiteTerm]\ngmpe_name = 'OceanicCan15Upp'"|[5, 14]    |
+-------+--------------------------------------------------+-----------+

Required parameters per tectonic region type
--------------------------------------------
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------+---------+----------+-----------+
| trt_smr|gsims                                                                                                                                                   |distances|siteparams|ruptparams |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------+---------+----------+-----------+
| 0      |"[NRCan15SiteTerm]\ngmpe_name = 'OceanicCan15Low'" "[NRCan15SiteTerm]\ngmpe_name = 'OceanicCan15Mid'" "[NRCan15SiteTerm]\ngmpe_name = 'OceanicCan15Upp'"|repi     |vs30      |mag rake   |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------+---------+----------+-----------+
| 1      |"[NRCan15SiteTerm]\ngmpe_name = 'OceanicCan15Low'" "[NRCan15SiteTerm]\ngmpe_name = 'OceanicCan15Mid'" "[NRCan15SiteTerm]\ngmpe_name = 'OceanicCan15Upp'"|repi     |vs30      |mag rake   |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------+---------+----------+-----------+
| 2      |"[NRCan15SiteTerm]\ngmpe_name = 'OceanicCan15Low'" "[NRCan15SiteTerm]\ngmpe_name = 'OceanicCan15Mid'" "[NRCan15SiteTerm]\ngmpe_name = 'OceanicCan15Upp'"|repi     |vs30      |mag rake   |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------+---------+----------+-----------+
| 3      |"[NRCan15SiteTerm]\ngmpe_name = 'OceanicCan15Low'" "[NRCan15SiteTerm]\ngmpe_name = 'OceanicCan15Mid'" "[NRCan15SiteTerm]\ngmpe_name = 'OceanicCan15Upp'"|repi     |vs30      |mag rake   |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------+---------+----------+-----------+
| 4      |"[NRCan15SiteTerm]\ngmpe_name = 'OceanicCan15Low'" "[NRCan15SiteTerm]\ngmpe_name = 'OceanicCan15Mid'" "[NRCan15SiteTerm]\ngmpe_name = 'OceanicCan15Upp'"|repi     |vs30      |mag rake   |
+--------+--------------------------------------------------------------------------------------------------------------------------------------------------------+---------+----------+-----------+

Exposure model
--------------
+------------+--+
| #assets    |2 |
+------------+--+
| #taxonomies|2 |
+------------+--+

+-----------+----------+-------+------+---+---+----------+
| taxonomy  |num_assets|mean   |stddev|min|max|num_sites |
+-----------+----------+-------+------+---+---+----------+
| RES1-W1-HC|1         |1.00000|nan   |1  |1  |1         |
+-----------+----------+-------+------+---+---+----------+
| RES1-W1-LC|1         |1.00000|nan   |1  |1  |1         |
+-----------+----------+-------+------+---+---+----------+
| *ALL*     |9         |0.22222|187%  |0  |1  |2         |
+-----------+----------+-------+------+---+---+----------+

Slowest sources
---------------
+----------+----+---------+---------+-------------+
| source_id|code|calc_time|num_sites|eff_ruptures |
+----------+----+---------+---------+-------------+
| OFS;1    |A   |0.09700  |2        |15_618       |
+----------+----+---------+---------+-------------+
| OFS;0    |A   |0.06021  |2        |8_778        |
+----------+----+---------+---------+-------------+

Computation times by source typology
------------------------------------
+-----+---------+---------+-------------+
| code|calc_time|num_sites|eff_ruptures |
+-----+---------+---------+-------------+
| A   |0.15722  |4        |24_396       |
+-----+---------+---------+-------------+

Information about the tasks
---------------------------
+-------------------+------+-------+------+-------+--------+
| operation-duration|counts|mean   |stddev|min    |max     |
+-------------------+------+-------+------+-------+--------+
| preclassical      |2     |0.09064|23%   |0.06919|0.11209 |
+-------------------+------+-------+------+-------+--------+
| read_source_model |5     |0.00270|14%   |0.00229|0.00319 |
+-------------------+------+-------+------+-------+--------+

Data transfer
-------------
+------------------+---------------------------------------------+---------+
| task             |sent                                         |received |
+------------------+---------------------------------------------+---------+
| read_source_model|converter=1.73 KB fname=535 B                |10.46 KB |
+------------------+---------------------------------------------+---------+
| preclassical     |srcs=3.68 KB srcfilter=2.68 KB params=1.72 KB|93.15 KB |
+------------------+---------------------------------------------+---------+

Slowest operations
------------------
+-------------------------+--------+---------+-------+
| calc_3403, maxmem=0.7 GB|time_sec|memory_mb|counts |
+-------------------------+--------+---------+-------+
| composite source model  |1.48406 |0.00781  |1      |
+-------------------------+--------+---------+-------+
| total preclassical      |0.18128 |0.70312  |2      |
+-------------------------+--------+---------+-------+
| splitting sources       |0.15769 |0.70312  |2      |
+-------------------------+--------+---------+-------+
| weighting sources       |0.02265 |0.0      |2      |
+-------------------------+--------+---------+-------+
| total read_source_model |0.01349 |0.45312  |5      |
+-------------------------+--------+---------+-------+
| reading exposure        |0.00531 |0.0      |1      |
+-------------------------+--------+---------+-------+