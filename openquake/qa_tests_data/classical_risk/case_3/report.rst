Classical PSHA - Loss fractions QA test
=======================================

+---------------+---------------------+
| checksum32    |3_603_069_573        |
+---------------+---------------------+
| date          |2021-05-02T09:28:36  |
+---------------+---------------------+
| engine_version|3.12.0-git9b6ffe086d |
+---------------+---------------------+

num_sites = 12, num_levels = 19, num_rlzs = 1

Parameters
----------
+--------------------------------+-------------------------------------------+
| calculation_mode               |'preclassical'                             |
+--------------------------------+-------------------------------------------+
| number_of_logic_tree_samples   |1                                          |
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
| width_of_mfd_bin               |0.2                                        |
+--------------------------------+-------------------------------------------+
| area_source_discretization     |10.0                                       |
+--------------------------------+-------------------------------------------+
| pointsource_distance           |None                                       |
+--------------------------------+-------------------------------------------+
| ground_motion_correlation_model|None                                       |
+--------------------------------+-------------------------------------------+
| minimum_intensity              |{'PGA': 0.01}                              |
+--------------------------------+-------------------------------------------+
| random_seed                    |23                                         |
+--------------------------------+-------------------------------------------+
| master_seed                    |123456789                                  |
+--------------------------------+-------------------------------------------+
| ses_seed                       |42                                         |
+--------------------------------+-------------------------------------------+

Input files
-----------
+-------------------------+-------------------------------------------------------------+
| Name                    |File                                                         |
+-------------------------+-------------------------------------------------------------+
| exposure                |`exposure_model.xml <exposure_model.xml>`_                   |
+-------------------------+-------------------------------------------------------------+
| gsim_logic_tree         |`gmpe_logic_tree.xml <gmpe_logic_tree.xml>`_                 |
+-------------------------+-------------------------------------------------------------+
| job_ini                 |`job.ini <job.ini>`_                                         |
+-------------------------+-------------------------------------------------------------+
| source_model_logic_tree |`source_model_logic_tree.xml <source_model_logic_tree.xml>`_ |
+-------------------------+-------------------------------------------------------------+
| structural_vulnerability|`vulnerability_model.xml <vulnerability_model.xml>`_         |
+-------------------------+-------------------------------------------------------------+

Composite source model
----------------------
+-------+-------------------+-----+
| grp_id|gsim               |rlzs |
+-------+-------------------+-----+
| 0     |'[ChiouYoungs2008]'|[0]  |
+-------+-------------------+-----+

Required parameters per tectonic region type
--------------------------------------------
+--------+-------------------+-----------+-----------------------+------------------+
| trt_smr|gsims              |distances  |siteparams             |ruptparams        |
+--------+-------------------+-----------+-----------------------+------------------+
| 0      |'[ChiouYoungs2008]'|rjb rrup rx|vs30 vs30measured z1pt0|dip mag rake ztor |
+--------+-------------------+-----------+-----------------------+------------------+

Exposure model
--------------
+------------+---+
| #assets    |13 |
+------------+---+
| #taxonomies|4  |
+------------+---+

+---------+----------+-------+------+---+---+----------+
| taxonomy|num_assets|mean   |stddev|min|max|num_sites |
+---------+----------+-------+------+---+---+----------+
| W       |5         |1.00000|0%    |1  |1  |5         |
+---------+----------+-------+------+---+---+----------+
| A       |4         |1.00000|0%    |1  |1  |4         |
+---------+----------+-------+------+---+---+----------+
| DS      |1         |2.00000|nan   |2  |2  |2         |
+---------+----------+-------+------+---+---+----------+
| UFB     |2         |1.00000|0%    |1  |1  |2         |
+---------+----------+-------+------+---+---+----------+
| *ALL*   |12        |1.08333|25%   |1  |2  |13        |
+---------+----------+-------+------+---+---+----------+

Slowest sources
---------------
+----------+----+---------+---------+-------------+
| source_id|code|calc_time|num_sites|eff_ruptures |
+----------+----+---------+---------+-------------+
| 232      |A   |0.19508  |8        |1_612        |
+----------+----+---------+---------+-------------+
| 225      |A   |0.04460  |2        |520          |
+----------+----+---------+---------+-------------+

Computation times by source typology
------------------------------------
+-----+---------+---------+-------------+
| code|calc_time|num_sites|eff_ruptures |
+-----+---------+---------+-------------+
| A   |0.24097  |10       |2_132        |
+-----+---------+---------+-------------+

Information about the tasks
---------------------------
+-------------------+------+-------+------+-------+--------+
| operation-duration|counts|mean   |stddev|min    |max     |
+-------------------+------+-------+------+-------+--------+
| preclassical      |1     |1.35991|nan   |1.35991|1.35991 |
+-------------------+------+-------+------+-------+--------+
| read_source_model |1     |0.04728|nan   |0.04728|0.04728 |
+-------------------+------+-------+------+-------+--------+

Data transfer
-------------
+------------------+----+---------+
| task             |sent|received |
+------------------+----+---------+
| read_source_model|    |7.92 KB  |
+------------------+----+---------+
| preclassical     |    |52.56 KB |
+------------------+----+---------+

Slowest operations
------------------
+-------------------------+--------+---------+-------+
| calc_3555, maxmem=0.5 GB|time_sec|memory_mb|counts |
+-------------------------+--------+---------+-------+
| total preclassical      |1.35991 |0.0      |1      |
+-------------------------+--------+---------+-------+
| weighting sources       |1.11778 |0.0      |1      |
+-------------------------+--------+---------+-------+
| splitting sources       |0.24156 |0.0      |1      |
+-------------------------+--------+---------+-------+
| composite source model  |0.14642 |0.0      |1      |
+-------------------------+--------+---------+-------+
| total read_source_model |0.04728 |0.0      |1      |
+-------------------------+--------+---------+-------+
| reading exposure        |0.00339 |0.0      |1      |
+-------------------------+--------+---------+-------+