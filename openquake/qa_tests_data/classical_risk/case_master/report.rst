classical risk
==============

+---------------+---------------------+
| checksum32    |1_454_271_571        |
+---------------+---------------------+
| date          |2021-05-02T09:28:40  |
+---------------+---------------------+
| engine_version|3.12.0-git9b6ffe086d |
+---------------+---------------------+

num_sites = 7, num_levels = 120, num_rlzs = 8

Parameters
----------
+--------------------------------+---------------------------------------------------------------------+
| calculation_mode               |'preclassical'                                                       |
+--------------------------------+---------------------------------------------------------------------+
| number_of_logic_tree_samples   |0                                                                    |
+--------------------------------+---------------------------------------------------------------------+
| maximum_distance               |{'default': [[1.0, 200.0], [10.0, 200.0]]}                           |
+--------------------------------+---------------------------------------------------------------------+
| investigation_time             |50.0                                                                 |
+--------------------------------+---------------------------------------------------------------------+
| ses_per_logic_tree_path        |1                                                                    |
+--------------------------------+---------------------------------------------------------------------+
| truncation_level               |3.0                                                                  |
+--------------------------------+---------------------------------------------------------------------+
| rupture_mesh_spacing           |2.0                                                                  |
+--------------------------------+---------------------------------------------------------------------+
| complex_fault_mesh_spacing     |2.0                                                                  |
+--------------------------------+---------------------------------------------------------------------+
| width_of_mfd_bin               |0.1                                                                  |
+--------------------------------+---------------------------------------------------------------------+
| area_source_discretization     |10.0                                                                 |
+--------------------------------+---------------------------------------------------------------------+
| pointsource_distance           |None                                                                 |
+--------------------------------+---------------------------------------------------------------------+
| ground_motion_correlation_model|None                                                                 |
+--------------------------------+---------------------------------------------------------------------+
| minimum_intensity              |{'PGA': 0.005, 'SA(0.1)': 0.005, 'SA(0.4)': 0.005, 'SA(0.3)': 0.005} |
+--------------------------------+---------------------------------------------------------------------+
| random_seed                    |24                                                                   |
+--------------------------------+---------------------------------------------------------------------+
| master_seed                    |123456789                                                            |
+--------------------------------+---------------------------------------------------------------------+
| ses_seed                       |42                                                                   |
+--------------------------------+---------------------------------------------------------------------+

Input files
-----------
+------------------------------------+---------------------------------------------------------------------------------+
| Name                               |File                                                                             |
+------------------------------------+---------------------------------------------------------------------------------+
| business_interruption_vulnerability|`downtime_vulnerability_model.xml <downtime_vulnerability_model.xml>`_           |
+------------------------------------+---------------------------------------------------------------------------------+
| contents_vulnerability             |`contents_vulnerability_model.xml <contents_vulnerability_model.xml>`_           |
+------------------------------------+---------------------------------------------------------------------------------+
| exposure                           |`exposure_model.xml <exposure_model.xml>`_                                       |
+------------------------------------+---------------------------------------------------------------------------------+
| gsim_logic_tree                    |`gsim_logic_tree.xml <gsim_logic_tree.xml>`_                                     |
+------------------------------------+---------------------------------------------------------------------------------+
| job_ini                            |`job.ini <job.ini>`_                                                             |
+------------------------------------+---------------------------------------------------------------------------------+
| nonstructural_vulnerability        |`nonstructural_vulnerability_model.xml <nonstructural_vulnerability_model.xml>`_ |
+------------------------------------+---------------------------------------------------------------------------------+
| occupants_vulnerability            |`occupants_vulnerability_model.xml <occupants_vulnerability_model.xml>`_         |
+------------------------------------+---------------------------------------------------------------------------------+
| source_model_logic_tree            |`source_model_logic_tree.xml <source_model_logic_tree.xml>`_                     |
+------------------------------------+---------------------------------------------------------------------------------+
| structural_vulnerability           |`structural_vulnerability_model.xml <structural_vulnerability_model.xml>`_       |
+------------------------------------+---------------------------------------------------------------------------------+

Composite source model
----------------------
+-------+---------------------+-------------+
| grp_id|gsim                 |rlzs         |
+-------+---------------------+-------------+
| 0     |'[BooreAtkinson2008]'|[0, 1, 4, 5] |
+-------+---------------------+-------------+
| 0     |'[ChiouYoungs2008]'  |[2, 3, 6, 7] |
+-------+---------------------+-------------+
| 1     |'[AkkarBommer2010]'  |[0, 2]       |
+-------+---------------------+-------------+
| 1     |'[ChiouYoungs2008]'  |[1, 3]       |
+-------+---------------------+-------------+
| 2     |'[AkkarBommer2010]'  |[4, 6]       |
+-------+---------------------+-------------+
| 2     |'[ChiouYoungs2008]'  |[5, 7]       |
+-------+---------------------+-------------+

Required parameters per tectonic region type
--------------------------------------------
+--------+-----------------------------------------+-----------+-----------------------+------------------+
| trt_smr|gsims                                    |distances  |siteparams             |ruptparams        |
+--------+-----------------------------------------+-----------+-----------------------+------------------+
| 0      |'[BooreAtkinson2008]' '[ChiouYoungs2008]'|rjb rrup rx|vs30 vs30measured z1pt0|dip mag rake ztor |
+--------+-----------------------------------------+-----------+-----------------------+------------------+
| 1      |'[BooreAtkinson2008]' '[ChiouYoungs2008]'|rjb rrup rx|vs30 vs30measured z1pt0|dip mag rake ztor |
+--------+-----------------------------------------+-----------+-----------------------+------------------+
| 2      |'[AkkarBommer2010]' '[ChiouYoungs2008]'  |rjb rrup rx|vs30 vs30measured z1pt0|dip mag rake ztor |
+--------+-----------------------------------------+-----------+-----------------------+------------------+
| 3      |'[AkkarBommer2010]' '[ChiouYoungs2008]'  |rjb rrup rx|vs30 vs30measured z1pt0|dip mag rake ztor |
+--------+-----------------------------------------+-----------+-----------------------+------------------+

Exposure model
--------------
+------------+--+
| #assets    |7 |
+------------+--+
| #taxonomies|3 |
+------------+--+

+---------+----------+-------+------+---+---+----------+
| taxonomy|num_assets|mean   |stddev|min|max|num_sites |
+---------+----------+-------+------+---+---+----------+
| tax1    |4         |1.00000|0%    |1  |1  |4         |
+---------+----------+-------+------+---+---+----------+
| tax2    |2         |1.00000|0%    |1  |1  |2         |
+---------+----------+-------+------+---+---+----------+
| tax3    |1         |1.00000|nan   |1  |1  |1         |
+---------+----------+-------+------+---+---+----------+
| *ALL*   |7         |1.00000|0%    |1  |1  |7         |
+---------+----------+-------+------+---+---+----------+

Slowest sources
---------------
+----------+----+---------+---------+-------------+
| source_id|code|calc_time|num_sites|eff_ruptures |
+----------+----+---------+---------+-------------+
| 1        |S   |0.00444  |7        |482          |
+----------+----+---------+---------+-------------+
| 2;0      |S   |0.00300  |7        |4            |
+----------+----+---------+---------+-------------+
| 2;1      |X   |2.079E-04|7        |1            |
+----------+----+---------+---------+-------------+

Computation times by source typology
------------------------------------
+-----+---------+---------+-------------+
| code|calc_time|num_sites|eff_ruptures |
+-----+---------+---------+-------------+
| S   |0.00744  |14       |486          |
+-----+---------+---------+-------------+
| X   |2.079E-04|7        |1            |
+-----+---------+---------+-------------+

Information about the tasks
---------------------------
+-------------------+------+-------+------+---------+--------+
| operation-duration|counts|mean   |stddev|min      |max     |
+-------------------+------+-------+------+---------+--------+
| preclassical      |3     |0.00496|60%   |9.012E-04|0.00798 |
+-------------------+------+-------+------+---------+--------+
| read_source_model |2     |0.00569|43%   |0.00324  |0.00814 |
+-------------------+------+-------+------+---------+--------+

Data transfer
-------------
+------------------+----------------------------------------------+---------+
| task             |sent                                          |received |
+------------------+----------------------------------------------+---------+
| read_source_model|converter=622 B fname=216 B                   |13.69 KB |
+------------------+----------------------------------------------+---------+
| preclassical     |srcs=14.15 KB srcfilter=4.37 KB params=2.36 KB|14.98 KB |
+------------------+----------------------------------------------+---------+

Slowest operations
------------------
+-------------------------+--------+---------+-------+
| calc_3557, maxmem=0.7 GB|time_sec|memory_mb|counts |
+-------------------------+--------+---------+-------+
| composite source model  |1.24595 |0.0      |1      |
+-------------------------+--------+---------+-------+
| total preclassical      |0.01489 |0.64453  |3      |
+-------------------------+--------+---------+-------+
| total read_source_model |0.01137 |0.29297  |2      |
+-------------------------+--------+---------+-------+
| splitting sources       |0.00837 |0.64453  |3      |
+-------------------------+--------+---------+-------+
| weighting sources       |0.00417 |0.0      |3      |
+-------------------------+--------+---------+-------+
| reading exposure        |0.00362 |0.0      |1      |
+-------------------------+--------+---------+-------+