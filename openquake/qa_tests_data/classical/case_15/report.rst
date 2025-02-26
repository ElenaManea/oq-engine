Classical PSHA with GMPE logic tree with multiple tectonic region types
=======================================================================

+---------------+---------------------+
| checksum32    |2_986_161_831        |
+---------------+---------------------+
| date          |2021-05-02T09:27:19  |
+---------------+---------------------+
| engine_version|3.12.0-git9b6ffe086d |
+---------------+---------------------+

num_sites = 3, num_levels = 10, num_rlzs = 12

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
| area_source_discretization     |10.0                                       |
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
| source_model_logic_tree|`source_model_logic_tree.xml <source_model_logic_tree.xml>`_ |
+------------------------+-------------------------------------------------------------+

Composite source model
----------------------
+-------+-------------------------+---------+
| grp_id|gsim                     |rlzs     |
+-------+-------------------------+---------+
| 0     |'[BooreAtkinson2008]'    |[0, 1]   |
+-------+-------------------------+---------+
| 0     |'[CampbellBozorgnia2008]'|[2, 3]   |
+-------+-------------------------+---------+
| 1     |'[BooreAtkinson2008]'    |[4, 5]   |
+-------+-------------------------+---------+
| 1     |'[CampbellBozorgnia2008]'|[6, 7]   |
+-------+-------------------------+---------+
| 2     |'[BooreAtkinson2008]'    |[8, 9]   |
+-------+-------------------------+---------+
| 2     |'[CampbellBozorgnia2008]'|[10, 11] |
+-------+-------------------------+---------+
| 3     |'[Campbell2003]'         |[0, 2]   |
+-------+-------------------------+---------+
| 3     |'[ToroEtAl2002]'         |[1, 3]   |
+-------+-------------------------+---------+

Required parameters per tectonic region type
--------------------------------------------
+--------+-----------------------------------------------+---------+----------+------------------+
| trt_smr|gsims                                          |distances|siteparams|ruptparams        |
+--------+-----------------------------------------------+---------+----------+------------------+
| 0      |'[BooreAtkinson2008]' '[CampbellBozorgnia2008]'|rjb rrup |vs30 z2pt5|dip mag rake ztor |
+--------+-----------------------------------------------+---------+----------+------------------+
| 1      |'[BooreAtkinson2008]' '[CampbellBozorgnia2008]'|rjb rrup |vs30 z2pt5|dip mag rake ztor |
+--------+-----------------------------------------------+---------+----------+------------------+
| 2      |'[BooreAtkinson2008]' '[CampbellBozorgnia2008]'|rjb rrup |vs30 z2pt5|dip mag rake ztor |
+--------+-----------------------------------------------+---------+----------+------------------+
| 3      |'[Campbell2003]' '[ToroEtAl2002]'              |rjb rrup |          |mag               |
+--------+-----------------------------------------------+---------+----------+------------------+
| 4      |'[Campbell2003]' '[ToroEtAl2002]'              |rjb rrup |          |mag               |
+--------+-----------------------------------------------+---------+----------+------------------+
| 5      |'[Campbell2003]' '[ToroEtAl2002]'              |rjb rrup |          |mag               |
+--------+-----------------------------------------------+---------+----------+------------------+

Slowest sources
---------------
+----------+----+---------+---------+-------------+
| source_id|code|calc_time|num_sites|eff_ruptures |
+----------+----+---------+---------+-------------+
| 3;0      |A   |0.00826  |3        |240          |
+----------+----+---------+---------+-------------+
| 3;1      |A   |0.00522  |3        |240          |
+----------+----+---------+---------+-------------+
| 1        |P   |3.276E-04|3        |15           |
+----------+----+---------+---------+-------------+
| 2        |P   |2.301E-04|3        |15           |
+----------+----+---------+---------+-------------+

Computation times by source typology
------------------------------------
+-----+---------+---------+-------------+
| code|calc_time|num_sites|eff_ruptures |
+-----+---------+---------+-------------+
| A   |0.01348  |6        |480          |
+-----+---------+---------+-------------+
| P   |5.577E-04|6        |30           |
+-----+---------+---------+-------------+

Information about the tasks
---------------------------
+-------------------+------+-------+------+-------+--------+
| operation-duration|counts|mean   |stddev|min    |max     |
+-------------------+------+-------+------+-------+--------+
| preclassical      |4     |0.00544|78%   |0.00117|0.01145 |
+-------------------+------+-------+------+-------+--------+
| read_source_model |2     |0.00236|36%   |0.00149|0.00322 |
+-------------------+------+-------+------+-------+--------+

Data transfer
-------------
+------------------+---------------------------------------------+---------+
| task             |sent                                         |received |
+------------------+---------------------------------------------+---------+
| read_source_model|converter=622 B fname=198 B                  |3.68 KB  |
+------------------+---------------------------------------------+---------+
| preclassical     |srcfilter=6.46 KB srcs=4.97 KB params=4.48 KB|11.85 KB |
+------------------+---------------------------------------------+---------+

Slowest operations
------------------
+-------------------------+--------+---------+-------+
| calc_3468, maxmem=0.7 GB|time_sec|memory_mb|counts |
+-------------------------+--------+---------+-------+
| composite source model  |1.28143 |0.0      |1      |
+-------------------------+--------+---------+-------+
| total preclassical      |0.02175 |0.37891  |4      |
+-------------------------+--------+---------+-------+
| splitting sources       |0.01510 |0.12891  |4      |
+-------------------------+--------+---------+-------+
| total read_source_model |0.00471 |0.32812  |2      |
+-------------------------+--------+---------+-------+
| weighting sources       |0.00457 |0.25000  |4      |
+-------------------------+--------+---------+-------+