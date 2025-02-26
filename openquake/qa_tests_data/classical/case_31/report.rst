Classical PSHA with source specific logic tree (3**2 realizations)
==================================================================

+---------------+---------------------+
| checksum32    |4_055_204_234        |
+---------------+---------------------+
| date          |2021-05-02T09:26:04  |
+---------------+---------------------+
| engine_version|3.12.0-git9b6ffe086d |
+---------------+---------------------+

num_sites = 1, num_levels = 14, num_rlzs = 9

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
| rupture_mesh_spacing           |5.0                                        |
+--------------------------------+-------------------------------------------+
| complex_fault_mesh_spacing     |5.0                                        |
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
+-------+---------------------+----------+
| grp_id|gsim                 |rlzs      |
+-------+---------------------+----------+
| 0     |'[BooreAtkinson2008]'|[0, 3, 6] |
+-------+---------------------+----------+
| 1     |'[BooreAtkinson2008]'|[1, 4, 7] |
+-------+---------------------+----------+
| 2     |'[BooreAtkinson2008]'|[2, 5, 8] |
+-------+---------------------+----------+
| 3     |'[ToroEtAl2002]'     |[0, 1, 2] |
+-------+---------------------+----------+
| 4     |'[ToroEtAl2002]'     |[3, 4, 5] |
+-------+---------------------+----------+
| 5     |'[ToroEtAl2002]'     |[6, 7, 8] |
+-------+---------------------+----------+

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
| 4      |'[BooreAtkinson2008]'|rjb      |vs30      |mag rake   |
+--------+---------------------+---------+----------+-----------+
| 5      |'[BooreAtkinson2008]'|rjb      |vs30      |mag rake   |
+--------+---------------------+---------+----------+-----------+
| 6      |'[BooreAtkinson2008]'|rjb      |vs30      |mag rake   |
+--------+---------------------+---------+----------+-----------+
| 7      |'[BooreAtkinson2008]'|rjb      |vs30      |mag rake   |
+--------+---------------------+---------+----------+-----------+
| 8      |'[BooreAtkinson2008]'|rjb      |vs30      |mag rake   |
+--------+---------------------+---------+----------+-----------+
| 9      |'[ToroEtAl2002]'     |rjb      |          |mag        |
+--------+---------------------+---------+----------+-----------+
| 10     |'[ToroEtAl2002]'     |rjb      |          |mag        |
+--------+---------------------+---------+----------+-----------+
| 11     |'[ToroEtAl2002]'     |rjb      |          |mag        |
+--------+---------------------+---------+----------+-----------+
| 12     |'[ToroEtAl2002]'     |rjb      |          |mag        |
+--------+---------------------+---------+----------+-----------+
| 13     |'[ToroEtAl2002]'     |rjb      |          |mag        |
+--------+---------------------+---------+----------+-----------+
| 14     |'[ToroEtAl2002]'     |rjb      |          |mag        |
+--------+---------------------+---------+----------+-----------+
| 15     |'[ToroEtAl2002]'     |rjb      |          |mag        |
+--------+---------------------+---------+----------+-----------+
| 16     |'[ToroEtAl2002]'     |rjb      |          |mag        |
+--------+---------------------+---------+----------+-----------+
| 17     |'[ToroEtAl2002]'     |rjb      |          |mag        |
+--------+---------------------+---------+----------+-----------+

Slowest sources
---------------
+----------+----+---------+---------+-------------+
| source_id|code|calc_time|num_sites|eff_ruptures |
+----------+----+---------+---------+-------------+
| 1;2      |A   |0.03622  |1        |1_040        |
+----------+----+---------+---------+-------------+
| 1;1      |A   |0.03526  |1        |1_040        |
+----------+----+---------+---------+-------------+
| 1;0      |A   |0.03492  |1        |1_040        |
+----------+----+---------+---------+-------------+
| 2;0      |S   |0.01843  |1        |310          |
+----------+----+---------+---------+-------------+
| 2;2      |S   |0.01797  |1        |310          |
+----------+----+---------+---------+-------------+
| 2;1      |S   |0.01758  |1        |310          |
+----------+----+---------+---------+-------------+

Computation times by source typology
------------------------------------
+-----+---------+---------+-------------+
| code|calc_time|num_sites|eff_ruptures |
+-----+---------+---------+-------------+
| A   |0.10640  |3        |3_120        |
+-----+---------+---------+-------------+
| S   |0.05398  |3        |930          |
+-----+---------+---------+-------------+

Information about the tasks
---------------------------
+-------------------+------+-------+------+-------+--------+
| operation-duration|counts|mean   |stddev|min    |max     |
+-------------------+------+-------+------+-------+--------+
| preclassical      |6     |0.06808|35%   |0.04074|0.09265 |
+-------------------+------+-------+------+-------+--------+
| read_source_model |1     |0.00384|nan   |0.00384|0.00384 |
+-------------------+------+-------+------+-------+--------+

Data transfer
-------------
+------------------+---------------------------------------------+---------+
| task             |sent                                         |received |
+------------------+---------------------------------------------+---------+
| read_source_model|                                             |2.49 KB  |
+------------------+---------------------------------------------+---------+
| preclassical     |srcfilter=9.02 KB srcs=7.77 KB params=6.72 KB|44.15 KB |
+------------------+---------------------------------------------+---------+

Slowest operations
------------------
+-------------------------+--------+---------+-------+
| calc_3429, maxmem=0.7 GB|time_sec|memory_mb|counts |
+-------------------------+--------+---------+-------+
| total preclassical      |0.40847 |0.81250  |6      |
+-------------------------+--------+---------+-------+
| weighting sources       |0.23626 |0.0      |6      |
+-------------------------+--------+---------+-------+
| splitting sources       |0.16215 |0.81250  |6      |
+-------------------------+--------+---------+-------+
| composite source model  |0.11815 |0.0      |1      |
+-------------------------+--------+---------+-------+
| total read_source_model |0.00384 |0.0      |1      |
+-------------------------+--------+---------+-------+