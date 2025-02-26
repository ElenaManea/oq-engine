Example of AvgPoeGMPE
=====================

+---------------+---------------------+
| checksum32    |775_491_060          |
+---------------+---------------------+
| date          |2021-05-02T09:26:22  |
+---------------+---------------------+
| engine_version|3.12.0-git9b6ffe086d |
+---------------+---------------------+

num_sites = 1, num_levels = 20, num_rlzs = 1

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
| truncation_level               |3.0                                        |
+--------------------------------+-------------------------------------------+
| rupture_mesh_spacing           |1.0                                        |
+--------------------------------+-------------------------------------------+
| complex_fault_mesh_spacing     |1.0                                        |
+--------------------------------+-------------------------------------------+
| width_of_mfd_bin               |0.2                                        |
+--------------------------------+-------------------------------------------+
| area_source_discretization     |10.0                                       |
+--------------------------------+-------------------------------------------+
| pointsource_distance           |None                                       |
+--------------------------------+-------------------------------------------+
| ground_motion_correlation_model|None                                       |
+--------------------------------+-------------------------------------------+
| minimum_intensity              |{}                                         |
+--------------------------------+-------------------------------------------+
| random_seed                    |1                                          |
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
+-------+---------------------------------------------------------------------------------+-----+
| grp_id|gsim                                                                             |rlzs |
+-------+---------------------------------------------------------------------------------+-----+
| 0     |'[AvgPoeGMPE]\nb1.AkkarEtAlRjb2014.weight = 0.4\nb2.ChiouYoungs2014.weight = 0.6'|[0]  |
+-------+---------------------------------------------------------------------------------+-----+

Required parameters per tectonic region type
--------------------------------------------
+--------+---------------------------------------------------------------------------------+-----------+-----------------------+------------------+
| trt_smr|gsims                                                                            |distances  |siteparams             |ruptparams        |
+--------+---------------------------------------------------------------------------------+-----------+-----------------------+------------------+
| 0      |'[AvgPoeGMPE]\nb1.AkkarEtAlRjb2014.weight = 0.4\nb2.ChiouYoungs2014.weight = 0.6'|rjb rrup rx|vs30 vs30measured z1pt0|dip mag rake ztor |
+--------+---------------------------------------------------------------------------------+-----------+-----------------------+------------------+

Slowest sources
---------------
+----------+----+---------+---------+-------------+
| source_id|code|calc_time|num_sites|eff_ruptures |
+----------+----+---------+---------+-------------+
| 001      |X   |3.314E-04|1        |1            |
+----------+----+---------+---------+-------------+

Computation times by source typology
------------------------------------
+-----+---------+---------+-------------+
| code|calc_time|num_sites|eff_ruptures |
+-----+---------+---------+-------------+
| X   |3.314E-04|1        |1            |
+-----+---------+---------+-------------+

Information about the tasks
---------------------------
+-------------------+------+-------+------+-------+--------+
| operation-duration|counts|mean   |stddev|min    |max     |
+-------------------+------+-------+------+-------+--------+
| preclassical      |1     |0.00134|nan   |0.00134|0.00134 |
+-------------------+------+-------+------+-------+--------+
| read_source_model |1     |0.00284|nan   |0.00284|0.00284 |
+-------------------+------+-------+------+-------+--------+

Data transfer
-------------
+------------------+----+---------+
| task             |sent|received |
+------------------+----+---------+
| read_source_model|    |2.19 KB  |
+------------------+----+---------+
| preclassical     |    |2.09 KB  |
+------------------+----+---------+

Slowest operations
------------------
+-------------------------+---------+---------+-------+
| calc_3441, maxmem=0.2 GB|time_sec |memory_mb|counts |
+-------------------------+---------+---------+-------+
| composite source model  |0.09031  |0.0      |1      |
+-------------------------+---------+---------+-------+
| total read_source_model |0.00284  |0.0      |1      |
+-------------------------+---------+---------+-------+
| total preclassical      |0.00134  |0.0      |1      |
+-------------------------+---------+---------+-------+
| splitting sources       |6.139E-04|0.0      |1      |
+-------------------------+---------+---------+-------+
| weighting sources       |1.955E-04|0.0      |1      |
+-------------------------+---------+---------+-------+