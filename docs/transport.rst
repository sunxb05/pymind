传输部分
*******

“传输部分”以萘分子晶体为例介绍了电荷传输的计算流程，按照步骤，分别对转移积分、重整能、随机行走等过程进行了详细的描述，同时加入了必要的 数据结果分析，简单易懂，便于理解。
  

输入文件
=======

1. 萘分子晶体结构文件
----------------------

准备萘分子晶体结构文件 naphthalene.cif(可以通过实验得到 cif 文件)。


.. code-block:: bash

	data_naphthalene
	_audit_creation_date              2019-05-20
	_audit_creation_method            'MOMAP'
	_symmetry_space_group_name_H-M    'P1'
	_symmetry_Int_Tables_number       1
	_symmetry_cell_setting            triclinic
	loop_
	_symmetry_equiv_pos_as_xyz
	  x,y,z
	_cell_length_a                    8.0980
	_cell_length_b                    5.9530
	_cell_length_c                    8.6520
	_cell_angle_alpha                 90.0000
	_cell_angle_beta                  124.4000
	_cell_angle_gamma                 90.0000
	loop_
	_atom_site_label
	_atom_site_type_symbol
	_atom_site_fract_x
	_atom_site_fract_y
	_atom_site_fract_z
	_atom_site_U_iso_or_equiv
	_atom_site_adp_type
	_atom_site_occupancy
	C1     C   0.082321   0.018562   0.328357  0.00000  Uiso   1.00
	C2     C   0.112956   0.163833   0.222892  0.00000  Uiso   1.00
	C3     C   0.047989   0.105174   0.037135  0.00000  Uiso   1.00
	C4     C   0.076558   0.251823  -0.075824  0.00000  Uiso   1.00
	C5     C  -0.013196  -0.190207   0.254606  0.00000  Uiso   1.00
	H6     H   0.124192   0.058895   0.455393  0.00000  Uiso   1.00
	H7     H   0.178710   0.305594   0.271107  0.00000  Uiso   1.00
	H8     H   0.141804   0.390694  -0.023603  0.00000  Uiso   1.00
	H9     H  -0.033302  -0.295196   0.331298  0.00000  Uiso   1.00
	C10    C  -0.047989  -0.105174  -0.037135  0.00000  Uiso   1.00
	C11    C  -0.112956  -0.163833  -0.222892  0.00000  Uiso   1.00
	C12    C  -0.082321  -0.018562  -0.328357  0.00000  Uiso   1.00
	C13    C  -0.076558  -0.251823   0.075824  0.00000  Uiso   1.00
	C14    C   0.013196   0.190207  -0.254606  0.00000  Uiso   1.00
	H15    H  -0.124192  -0.058895  -0.455393  0.00000  Uiso   1.00
	H16    H  -0.178710  -0.305594  -0.271107  0.00000  Uiso   1.00
	H17    H  -0.141804  -0.390694   0.023603  0.00000  Uiso   1.00
	H18    H   0.033302   0.295196  -0.331298  0.00000  Uiso   1.00
	C19    C   0.417679   0.518562  -0.328357  0.00000  Uiso   1.00
	C20    C   0.387044   0.663833  -0.222892  0.00000  Uiso   1.00
	C21    C   0.452011   0.605174  -0.037135  0.00000  Uiso   1.00
	C22    C   0.423442   0.751823   0.075824  0.00000  Uiso   1.00
	C23    C   0.513196   0.309793  -0.254606  0.00000  Uiso   1.00
	H24    H   0.375808   0.558895  -0.455393  0.00000  Uiso   1.00
	H25    H   0.321290   0.805594  -0.271107  0.00000  Uiso   1.00
	H26    H   0.358196   0.890694   0.023603  0.00000  Uiso   1.00
	H27    H   0.533302   0.204804  -0.331298  0.00000  Uiso   1.00
	C28    C   0.547989   0.394826   0.037135  0.00000  Uiso   1.00
	C29    C   0.612956   0.336167   0.222892  0.00000  Uiso   1.00
	C30    C   0.582321   0.481438   0.328357  0.00000  Uiso   1.00
	C31    C   0.576558   0.248177  -0.075824  0.00000  Uiso   1.00
	C32    C   0.486804   0.690207   0.254606  0.00000  Uiso   1.00
	H33    H   0.624192   0.441105   0.455393  0.00000  Uiso   1.00
	H34    H   0.678710   0.194406   0.271107  0.00000  Uiso   1.00
	H35    H   0.641804   0.109306  -0.023603  0.00000  Uiso   1.00
	H36    H   0.466698   0.795196   0.331298  0.00000  Uiso   1.00



2. 输入文件
-----------


.. code-block:: bash

	&transport
	  do_transport_prepare              = 1     # 是否生成预备文件, 1表示开启，0表示关闭
	  do_transport_submit_HL_job        = 1     # 是否开启计算转移积分, 1表示开启，0表示关闭
	  do_transport_get_transferintegral = 1     # 计算计算转移积分, 1表示开启，0表示关闭
	  do_transport_submit_RE_job        = 1     # 计算重整能, 1表示开启，0表示关闭
	  do_transport_get_re_evc           = 1     # 使用 evc 程序分析重整能, 1表示开启，0表示关闭
	  do_transport_run_MC               = 1     # Monte Carlo 模拟, 1表示开启，0表示关闭
	  do_transport_get_mob_MC           = 1     # 计算迁移率, 1表示开启，0表示关闭
	  do_transport_run_MC_temp          = 0     # 不同温度下的Monte Carlo 模拟, 1表示开启，0表示关闭
	  do_transport_get_mob_MC_temp      = 0     # 计算不同温度下的迁移率, 1表示开启，0表示关闭
	  do_transport_run_ME               = 0     # ME 方法模拟, 1表示开启，0表示关闭
	  do_transport_get_mob_ME           = 0     # ME 方法计算迁移率, 1表示开启，0表示关闭
	  do_transport_run_ME_temp          = 0     # 不同温度下的 ME 模拟, 1表示开启，0表示关闭
	  do_transport_get_mob_ME_temp      = 0     # 计算不同温度下的迁移率, 1表示开启，0表示关闭
	  do_transport_gather_momap_data    = 0	    # 收集计算的相关数据, 1表示开启，0表示关闭

	  # Job Scheduling 
	  queue_name      = workq                   # 计算任务提交队列
	  sched_type      = local                   # pbs, slurm, lsf, or local， 作业管理系统

	  compute_engine  = 1                       # 1 = Gaussian, 2 = ORCA, 3 = QCHEM， 4 = BDF， 定义使用的计算引擎
	  qc_exe          = g09                     # g09/g16 or fullpath/orca or qchem or BDF， 计算引擎可执行程序

	  module_mpich2 = momap/devel               # MOMAP安装路径
	  module_qc = gaussian/g09.e01	            # 计算引擎路径

	  qc_method       = b3lyp                   # 计算所用方法
	  qc_basis        = b3lyp cc-pvdz           # 计算所用基组
	  qc_basis_re     = b3lyp cc-pvdz           # 计算重组能所用基组
	  qc_memory       = 4096                    # 计算引擎所用内存（in MB）
	  qc_nodes        = 1                       # 计算引擎申请使用节点数
	  qc_ppn          = 20                      # 计算引擎每节点并行运行核数
	   

	  temp            = 300	                    # 定义模拟温度

	  # Temperature Dependence
	  start_temp      = 200                     # 计算不同温度下的电荷迁移率时，定义模拟初始温度
	  end_temp        = 300                     # 计算不同温度下的电荷迁移率时，定义模拟最终温度
	  delta_temp      = 50	                    # 定义模拟温度间隔

	  ratetype        = quantum                 # marcus or quantum，定义电子空穴迁移速率计算方法

	  lat_cutoff      = 4                       # 计算相邻转移积分的截断半径(单位:Å)	
          super-cell      = 4 4 4                   # Monte Carlo 模拟超胞大小的三维尺寸

	  nsimu           = 2000                    # 定义总模拟次数
	  tsimu           = 1000                    # 定义总模拟时间（in ns）
	  tsnap           = 5	                    # 定义记录输出文件中的载流子位置的时间间隔

	  crystal         = naphthalene.cif         # 晶体文件
	/


执行以下命令运行程序:

	``momap –input momap.inp –nodefile nodefile``



.. seealso ::

	 对以上MOMAP输入变量的解释，请参考API Reference_ 部分


计算过程解释
============

文件 momap.inp 按照迁移率计算的的原理定义了不同步骤。


1. 生成预备文件
----------------


计算的第一步需要产生重整能和转移积分计算的 Gaussian 输入文件，在文件 momap.inp 中设置此步骤的开关:
注明: 1 是打开指令 0 是关闭指令

.. code-block:: bash

	do_transport_prepare              = 1       # 是否生成预备文件, 1表示开启，0表示关闭


可以得到萘分子近邻文件: 

* neighbor01.xyz
* neighbor02.xyz
* NEIGHBOR.dat
* SYS.dat
* 01/
* 02/


其中 neighbor01.xyz，neighbor02.xyz 的文件分别是第一个和第二个分子的近邻信息。目录 01/，02/下存有 Gaussian 输入文件。NEIGHBOR.dat，SYS.dat 是所有分子近邻信息的文件。


.. seealso ::

	对生成的文件的详细解释，请参考附录 appendix_ 部分


2. 计算转移积分和重整能
--------------------


.. code-block:: bash

    do_transport_submit_HL_job        = 1       # 是否开启计算转移积分, 1表示开启，0表示关闭
    do_transport_get_transferintegral = 1       # 计算计算转移积分, 1表示开启，0表示关闭
    do_transport_submit_RE_job        = 1       # 计算重整能, 1表示开启，0表示关闭


通过调用 scr 目录下的两个 python 脚本 mol_one.py 和 mol_two.py 来完成单分子单点能量计算和双分子单点能量计算。这两个 python 脚本设置运行锁并提交传输积分计算的作业。
当一个作业完成后，它会自动移除相应的锁。


计算完成后会产生 Gaussian 计算得到的重整能和转移积分计算结果，文件存放在目录 ``RE/`` 下的 log 和 fchk 文件中。其中 VH01.dat，VH02.dat，VL01.dat，VL02.dat 文件，可以得到 01、02 分子和 4 个近邻间的 HUMO 和 LOMO 能级的转移积分。同时在 ``transferintegral/`` 目录下得到不同分子与紧邻间的 HOMO 和 LUMO 能级的转移积分: 01/H.dat，01/L.dat，02/H.dat，02/L.dat。其中 01、02 表示第一、第二个分子。H和L分别代表HOMO和LUMO能级。


当转移积分计算完成后，所有与转移积分计算相关的锁将被清除。 MOMAP将很快提交重组能量计算的作业。 与计算转移积分计算相比，此步骤需要更多时间才能完成。


.. note ::

	可以在此步骤中添加更多选项。例如，如果想利用已经优化的不带电分子结构作为初始结构来优化相应阴离子阳离子的几何结构，可以将参数 RE_use_neutral_chk 设置为 1，即 ``RE_use_neutral_chk = 1``。

	另外，如果想利用Nelson四点法计算重组能，可以将参数RE_calc_lambda_4P设置为1，即 
	``RE_calc_lambda_4P = 1`` ，该方法可以用来检验evc计算中的重组能是否可靠。


通过调用 python脚本 ``scr/get_transint.py``，我们得到了传输积分数据 VH.dat 和 VL.dat，用于后面的传输跳跃率计算。

上述计算实际上使用了数据目录下的文件 trans_int_files.dat 中列出的信息。 例如，trans_int_files.dat 的内容可能如下所示:

.. image:: ./img/trans_int_files.png

第一行包含晶胞中的分子数，然后是中心单元中每个分子的邻居数目，加上三文件组列表和两个分子的ID。 这些文件由 MOMAP 可执行文件 transport_transferintegral.exe 使用。


3. 分析重整能
------------


.. code-block:: bash

	do_transport_get_re_evc           = 1       # 使用 evc 程序分析重整能, 1表示开启，0表示关闭


在这一步中，我们将计算分为三步：prepare_RE.py、run_RE.py 和 get_RE.py。首先是准备输入文件，接着调用 evc.exe 进行实际计算，第三部分是收集计算结果.

在目录 ``evc/`` 目录下文件 lamda.dat 存有电子和空穴重整能。其中 lam1 是指电 中性的分子处在平衡结构上和在带点结构上的能量之差。lam2 是指带电的离子 处在平衡结构和在电中性的分子上的能量之差。

目录 ``evc/elec/`` 下的 NM.dat 文件包含不同振动频率下的重整能和黄昆因子:

.. image:: ./img/t_p_1.png

用第一列和第二列可以画出振动频率和重整能的关系:

.. image:: ./img/t_p_2.png


4. 随机行走模拟
--------------------

这一步使用了蒙特卡罗的方法模拟了电子运动的轨迹，并由此计算迁移率

.. code-block:: bash

	do_transport_run_MC               = 1        # Monte Carlo 模拟, 1表示开启，0表示关闭
	do_transport_get_mob_MC           = 1        # 计算迁移率, 1表示开启，0表示关闭


计算后得到不同近邻间 HOMO、LUMO 能级迁移速率，分别在文件 WH01.dat，WH02.dat，WL01.dat，WL02.dat 中。

完成上述准备工作后，我们就可以进行 MC 模拟来计算电荷载流子迁移率。

这一步也分为两部分，即 prepare-mc.py 和 run_mc_batch.py。 第一部分是将得到的相关输入文件（如VH.dat、VL.dat、NM-e.dat NM-h.dat）复制到 MC 工作目录中，计算 hopping rate。 第二部分是 MC 模拟。 当 MC 程序运行时，生成的记录行走轨迹的文件被写到相应目录中。 通常，2000 条随机行走轨迹将给出合理的迁移率的结果。



.. important ::

   	在此步骤中，我们通常利用 OpenMP 做高速并行计算，它几乎与节点中的核数成线性比例关系。 例如，如果正在运行的节点有 28 个核，则运行速度是相应串行作业的 28 倍。


一旦 MC 模拟完成，我们就可以使用爱因斯坦关系从 MC 轨迹文件中计算随机游走迁移率。

其中 mob-e-all.dat 和 mob-h-all.dat 分别是电子和空穴在各个方向上的迁移率。下图是空穴在各个方向上的迁移率的部分内容:

.. image:: ./img/t_p_3.png

选取所需数据，可以画出 xy 平面上的空穴各向异性的迁移率:


.. image:: ./img/t_p_4.png


5. 不同温度下随机行走模拟
---------------------------

用户也可以使用蒙特卡罗的方法模拟不同温度情况下的电子运动的轨迹，并由此计算迁移率

.. code-block:: bash

	do_transport_run_MC_temp          = 1        # 不同温度下的Monte Carlo 模拟, 1表示开启，0表示关闭
	do_transport_get_mob_MC_temp      = 1        # 计算不同温度下的迁移率, 1表示开启，0表示关闭


计算得到的电子和空穴迁移率分别在目录 MC-quantu-temp (或者 MC-marcus-temp) 下的 mob-e.dat 和 mob-h.dat 文件中。
如下所示是电子在不同 温度下的迁移率及其误差值 mob-e.dat:

.. image:: ./img/t_p_5.png

使用上面的数据，可以画出电子、空穴的迁移率和温度的关系。下图所示为电子迁移率与温度的关系:

.. image:: ./img/t_p_6.png

6. 数据收集
-----------


当所有计算完成后，结果将收集到文件 momap.dat 中，如下所示。


.. image:: ./img/gather_data.png


计算结果作图
============

如果正确安装 ps2png 程序，我们可以使用以下命令生成和显示相应的 3D 和 2D 的结果图：

.. code-block:: bash

	$> gnuplot *.gnu
	$> ps2png *.eps
	$> display *.png


如果安装的 gnuplot 支持 pngcairo，我们可以简单地运行：

.. code-block:: bash

	$> gnuplot *.gnu-png
	$> display *.png



.. image:: ./img/plot_1.png
.. image:: ./img/plot_2.png


此外，如果 numpy 和 matplotlib 已安装，我们还可以使用生成的 python 脚本来显示电子迁移结果。 运行MC目录对应的python脚本为：mob_direction_all.py、mob_plane_xy.py、mob_plane_xz.py 和 mob_plane_yz.py。 例如，电子迁移的 3D 和 2D 图如下所示:



.. image:: ./img/plot_3.png
.. image:: ./img/plot_4.png



.. _Reference: https://pyminds.readthedocs.io/en/latest/autoapi/index.html
.. _appendix: https://pyminds.readthedocs.io/en/latest/appendix.html