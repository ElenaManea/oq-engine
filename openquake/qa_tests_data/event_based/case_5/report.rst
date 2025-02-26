Germany_SHARE Combined Model event_based
========================================

+---------------+---------------------+
| checksum32    |307_026_790          |
+---------------+---------------------+
| date          |2021-05-02T09:25:21  |
+---------------+---------------------+
| engine_version|3.12.0-git9b6ffe086d |
+---------------+---------------------+

num_sites = 100, num_levels = 1, num_rlzs = 15

Parameters
----------
+--------------------------------+-----------------------------------------+
| calculation_mode               |'preclassical'                           |
+--------------------------------+-----------------------------------------+
| number_of_logic_tree_samples   |0                                        |
+--------------------------------+-----------------------------------------+
| maximum_distance               |{'default': [[1.0, 80.0], [10.0, 80.0]]} |
+--------------------------------+-----------------------------------------+
| investigation_time             |30.0                                     |
+--------------------------------+-----------------------------------------+
| ses_per_logic_tree_path        |1                                        |
+--------------------------------+-----------------------------------------+
| truncation_level               |3.0                                      |
+--------------------------------+-----------------------------------------+
| rupture_mesh_spacing           |5.0                                      |
+--------------------------------+-----------------------------------------+
| complex_fault_mesh_spacing     |5.0                                      |
+--------------------------------+-----------------------------------------+
| width_of_mfd_bin               |0.1                                      |
+--------------------------------+-----------------------------------------+
| area_source_discretization     |18.0                                     |
+--------------------------------+-----------------------------------------+
| pointsource_distance           |None                                     |
+--------------------------------+-----------------------------------------+
| ground_motion_correlation_model|None                                     |
+--------------------------------+-----------------------------------------+
| minimum_intensity              |{}                                       |
+--------------------------------+-----------------------------------------+
| random_seed                    |42                                       |
+--------------------------------+-----------------------------------------+
| master_seed                    |123456789                                |
+--------------------------------+-----------------------------------------+
| ses_seed                       |23                                       |
+--------------------------------+-----------------------------------------+

Input files
-----------
+------------------------+-------------------------------------------------------------------------------+
| Name                   |File                                                                           |
+------------------------+-------------------------------------------------------------------------------+
| gsim_logic_tree        |`complete_gmpe_logic_tree.xml <complete_gmpe_logic_tree.xml>`_                 |
+------------------------+-------------------------------------------------------------------------------+
| job_ini                |`job.ini <job.ini>`_                                                           |
+------------------------+-------------------------------------------------------------------------------+
| sites                  |`sites.csv <sites.csv>`_                                                       |
+------------------------+-------------------------------------------------------------------------------+
| source_model_logic_tree|`combined_logic-tree-source-model.xml <combined_logic-tree-source-model.xml>`_ |
+------------------------+-------------------------------------------------------------------------------+

Composite source model
----------------------
+-------+----------------------+---------------------+
| grp_id|gsim                  |rlzs                 |
+-------+----------------------+---------------------+
| 0     |'[FaccioliEtAl2010]'  |[0, 1, 2, 3, 4]      |
+-------+----------------------+---------------------+
| 1     |'[FaccioliEtAl2010]'  |[10, 11, 12, 13, 14] |
+-------+----------------------+---------------------+
| 2     |'[AkkarBommer2010]'   |[5]                  |
+-------+----------------------+---------------------+
| 2     |'[Campbell2003SHARE]' |[9]                  |
+-------+----------------------+---------------------+
| 2     |'[CauzziFaccioli2008]'|[6]                  |
+-------+----------------------+---------------------+
| 2     |'[ChiouYoungs2008]'   |[7]                  |
+-------+----------------------+---------------------+
| 2     |'[ToroEtAl2002SHARE]' |[8]                  |
+-------+----------------------+---------------------+

Required parameters per tectonic region type
--------------------------------------------
+--------+----------------------------------------------------------------------------------------------------------+-----------------+-----------------------+------------------+
| trt_smr|gsims                                                                                                     |distances        |siteparams             |ruptparams        |
+--------+----------------------------------------------------------------------------------------------------------+-----------------+-----------------------+------------------+
| 0      |'[AkkarBommer2010]' '[Campbell2003SHARE]' '[CauzziFaccioli2008]' '[ChiouYoungs2008]' '[ToroEtAl2002SHARE]'|rhypo rjb rrup rx|vs30 vs30measured z1pt0|dip mag rake ztor |
+--------+----------------------------------------------------------------------------------------------------------+-----------------+-----------------------+------------------+
| 1      |'[AkkarBommer2010]' '[Campbell2003SHARE]' '[CauzziFaccioli2008]' '[ChiouYoungs2008]' '[ToroEtAl2002SHARE]'|rhypo rjb rrup rx|vs30 vs30measured z1pt0|dip mag rake ztor |
+--------+----------------------------------------------------------------------------------------------------------+-----------------+-----------------------+------------------+
| 2      |'[AkkarBommer2010]' '[Campbell2003SHARE]' '[CauzziFaccioli2008]' '[ChiouYoungs2008]' '[ToroEtAl2002SHARE]'|rhypo rjb rrup rx|vs30 vs30measured z1pt0|dip mag rake ztor |
+--------+----------------------------------------------------------------------------------------------------------+-----------------+-----------------------+------------------+
| 3      |'[FaccioliEtAl2010]'                                                                                      |rrup             |vs30                   |mag rake          |
+--------+----------------------------------------------------------------------------------------------------------+-----------------+-----------------------+------------------+
| 4      |'[FaccioliEtAl2010]'                                                                                      |rrup             |vs30                   |mag rake          |
+--------+----------------------------------------------------------------------------------------------------------+-----------------+-----------------------+------------------+
| 5      |'[FaccioliEtAl2010]'                                                                                      |rrup             |vs30                   |mag rake          |
+--------+----------------------------------------------------------------------------------------------------------+-----------------+-----------------------+------------------+

Slowest sources
---------------
+----------+----+---------+---------+-------------+
| source_id|code|calc_time|num_sites|eff_ruptures |
+----------+----+---------+---------+-------------+
| 263      |A   |0.02507  |2        |1_022        |
+----------+----+---------+---------+-------------+
| 264      |A   |0.02479  |2        |1_022        |
+----------+----+---------+---------+-------------+
| 19       |S   |0.02349  |9        |349          |
+----------+----+---------+---------+-------------+
| 250      |A   |0.01363  |6        |384          |
+----------+----+---------+---------+-------------+
| 248      |A   |0.01325  |6        |384          |
+----------+----+---------+---------+-------------+
| 249      |A   |0.01324  |6        |384          |
+----------+----+---------+---------+-------------+
| 20       |S   |0.00841  |9        |31           |
+----------+----+---------+---------+-------------+
| 22       |S   |0.00674  |1        |34           |
+----------+----+---------+---------+-------------+
| 246      |A   |0.00517  |10       |156          |
+----------+----+---------+---------+-------------+
| 247      |A   |0.00514  |10       |156          |
+----------+----+---------+---------+-------------+
| 21       |S   |0.00504  |9        |7            |
+----------+----+---------+---------+-------------+
| 1339     |A   |0.00500  |12       |168          |
+----------+----+---------+---------+-------------+
| 257      |A   |0.00398  |9        |96           |
+----------+----+---------+---------+-------------+
| 258      |A   |0.00376  |9        |96           |
+----------+----+---------+---------+-------------+
| 259      |A   |0.00372  |9        |96           |
+----------+----+---------+---------+-------------+
| 1        |A   |0.00181  |8        |7            |
+----------+----+---------+---------+-------------+
| 2        |A   |0.00140  |8        |7            |
+----------+----+---------+---------+-------------+
| 330045   |P   |2.315E-04|7        |22           |
+----------+----+---------+---------+-------------+
| 330046   |P   |9.346E-05|5        |20           |
+----------+----+---------+---------+-------------+
| 330051   |P   |8.368E-05|16       |34           |
+----------+----+---------+---------+-------------+

Computation times by source typology
------------------------------------
+-----+---------+---------+-------------+
| code|calc_time|num_sites|eff_ruptures |
+-----+---------+---------+-------------+
| A   |0.11997  |97       |3_978        |
+-----+---------+---------+-------------+
| P   |0.00278  |277      |640          |
+-----+---------+---------+-------------+
| S   |0.04369  |28       |421          |
+-----+---------+---------+-------------+

Information about the tasks
---------------------------
+-------------------+------+-------+------+-------+--------+
| operation-duration|counts|mean   |stddev|min    |max     |
+-------------------+------+-------+------+-------+--------+
| preclassical      |3     |0.10390|134%  |0.00447|0.30118 |
+-------------------+------+-------+------+-------+--------+
| read_source_model |3     |0.01040|54%   |0.00288|0.01668 |
+-------------------+------+-------+------+-------+--------+

Data transfer
-------------
+------------------+-----------------------------------------------+----------+
| task             |sent                                           |received  |
+------------------+-----------------------------------------------+----------+
| read_source_model|converter=1017 B fname=353 B                   |32.99 KB  |
+------------------+-----------------------------------------------+----------+
| preclassical     |srcs=36.93 KB srcfilter=19.11 KB params=4.84 KB|104.38 KB |
+------------------+-----------------------------------------------+----------+

Slowest operations
------------------
+-------------------------+--------+---------+-------+
| calc_3396, maxmem=0.6 GB|time_sec|memory_mb|counts |
+-------------------------+--------+---------+-------+
| composite source model  |1.21209 |0.34766  |1      |
+-------------------------+--------+---------+-------+
| total preclassical      |0.31171 |0.75000  |3      |
+-------------------------+--------+---------+-------+
| splitting sources       |0.16785 |0.75000  |3      |
+-------------------------+--------+---------+-------+
| weighting sources       |0.14224 |0.63672  |3      |
+-------------------------+--------+---------+-------+
| total read_source_model |0.03120 |0.84766  |3      |
+-------------------------+--------+---------+-------+