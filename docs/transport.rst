传输部分
*******

“传输部分”以萘分子晶体为例介绍了电荷传输的计算流程，按照步骤，分别对转移积分、重整能、随机行走等过程进行了详细的描述，同时加入了必要的 数据结果分析，简单易懂，便于理解。
  

输入文件
=======
吸收光谱、荧光光谱以及辐射速率的计算流程以 azulene 为例，算例数据位于 momap/example/azulene/目录下。

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


本算例部分计算文件在 azulene/gaussian/目录下。Gaussian 使用方法详见 Gaussian 手册。
以下为使用Gaussian进行基态构型优化与频率计算的输入文件的例子：

.. code-block:: bash

	&transport
	  do_transport_prepare              = 1
	  do_transport_submit_HL_job        = 1
	  do_transport_get_transferintegral = 1
	  do_transport_submit_RE_job        = 1
	  do_transport_get_re_evc           = 1
	  do_transport_run_MC               = 1
	  do_transport_get_mob_MC           = 1
	  do_transport_run_MC_temp          = 0
	  do_transport_get_mob_MC_temp      = 0
	  do_transport_run_ME               = 0
	  do_transport_get_mob_ME           = 0
	  do_transport_run_ME_temp          = 0
	  do_transport_get_mob_ME_temp      = 0
	  do_transport_gather_momap_data    = 0	

	  # Job Scheduling
	  queue_name      = workq
	  sched_type      = local    ! pbs, slurm, lsf, or local	

	  compute_engine  = 1      ! 1 = Gaussian, 2 = ORCA, 3 = QCHEM
	  qc_exe          = g09    ! g09/g16 or fullpath/orca or qchem	

	  module_mpich2 = momap/devel
	  module_qc = gaussian/g09.e01	

	  qc_method       = b3lyp
	  qc_basis        = b3lyp cc-pvdz
	  qc_basis_re     = b3lyp cc-pvdz
	  qc_memory       = 4096  ! MB
	  qc_nodes        = 1
	  qc_ppn          = 20
	  
	  RE_use_neutral_chk = 1
	# RE_calc_lambda_4P = 1
	# lat_site_energy = 1
	# app_elec_F      = 1e8 0 0	

	  temp            = 300	

	  # Temperature Dependence
	  start_temp      = 200
	  end_temp        = 300
	  delta_temp      = 50	

	  ratetype        = quantum  ! marcus or quantum	

	  lat_cutoff      = 4       ! for neighbor list construction	

	  nsimu           = 2000
	  tsimu           = 1000    ! in ns
	  tsnap           = 5	

	  crystal         = naphthalene.cif
	/


执行以下命令运行 EVC 振动分析程序:

	``momap –input momap.inp –nodefile nodefile``

程序正常结束后，得到下一步计算的输入文件 evc.cart.dat。



.. seealso ::

	 对以上MOMAP输入变量的解释，请参考API Reference部分.



.. important ::

   	MOMAP支持并行运算，如果使用队列脚本(如 PBS 脚本)提交任务，则只需在 PBS 脚本中修改提交队列名称、使用节点数量和核数量。

   	如果不使用队列脚本，可以在 nodefile 里 指定节点名称和核数。例如:需要使用节点名称为 node1 和 node2 的两个节点，每个节点上使用 2 个核。则 nodefile 写为 ::

	    node1 	
	    node1 	
	    node2 	
	    node2




计算结束后得到 azulene-s1.chk 和 azulene-s1.log 输出文件。
使用以下指令对二进制的 checkpoint 文件进行转换: 

	``formchk azulene-s1.chk``

运行结束后生成文件 azulene-s1.fchk，azulene-s1.flog 和 azulene-s1.fchk 这两个文件将用于后续的振动分析计算。




计算过程
========


1. 生成预备文件文件
----------------



计算的第一步需要产生重整能和转移积分计算的 Gaussian 输入文件，在文件 momap.inp 中设置此步骤的开关:
注明:1 是打开指令 0 是关闭指令

.. code-block:: bash

	do_evc          = 1                      # 1 表示开启dushin计算，0 表示关闭

	&evc
	  ffreq(1)      = "azulene-s0.log"       #基态结果的日志文件
	  ffreq(2)      = "azulene-s1.log"       #激发态结果的日志文件
	/


执行以下命令运行 EVC 振动分析程序:

	``momap –input momap.inp –nodefile nodefile``

程序正常结束后，得到下一步计算的输入文件 evc.cart.dat。



.. seealso ::

	 对以上MOMAP输入变量的解释，请参考API Reference部分.



.. important ::

   	MOMAP支持并行运算，如果使用队列脚本(如 PBS 脚本)提交任务，则只需在 PBS 脚本中修改提交队列名称、使用节点数量和核数量。

   	如果不使用队列脚本，可以在 nodefile 里 指定节点名称和核数。例如:需要使用节点名称为 node1 和 node2 的两个节点，每个节点上使用 2 个核。则 nodefile 写为 ::

	    node1 	
	    node1 	
	    node2 	
	    node2





3. 辐射速率
----------


a. 辐射速率输入文件 momap.inp:
++++++++++++++++++++++++++++

.. code-block:: bash

	do_spec_tvcf_ft   = 1                   #1 表示开启计算荧光关联函数
	do_spec_tvcf_spec = 1	                #1 表示开启计算荧光光谱

	&spec_tvcf                              #描述计算内容
	  DUSHIN        True                    #是否考虑 Duschinsky 转动(t 开启，f 关闭)
	  Temp          300                     #温度
	  tmax          1000                    #积分时间
	  dt            1                       #积分步长
	  Ead           0.07509                 #绝热激发能
	  EDMA          0.92694                 #吸收跃迁偶极矩
	  EDME          0.64751                 #发射跃迁偶极矩
	  FreqScale     1.0                     #频率缩放因子
	  DSFile        "evc.cart.dat"          #定义读取的 evc 文件名
	  Emax          0.3 au                  #定义光谱频率范围上限
	  dE            0.00001                 #定义输出能量间隔
	  logFile       "spec.tvcf.log"         #定义输出 log 文件名
	  FtFile        "spec.tvcf.ft.dat"      #定义输出的关联函数文件名
	  FoFile        "spec.tvcf.fo.dat"      #谱函数输出文件
	  FoSFile       "spec.tvcf.spec.dat"    #归一化的光谱输出文件
	/


.. seealso ::

	 对以上MOMAP输入变量的解释，请参考API Reference部分.


把 momap.inp 文件、nodefile 文件和 4.1.2 部分计算得到的 evc.cart.dat 文件 放置于同一目录，运行以下命令进行计算:

	``momap –input momap.inp –nodefile nodefile``



b. 计算结果解读:
+++++++++++++++++++

运行结束后会得到结果文件：

.. csv-table::
    :header: "输出文件名", "输出文件内容"

      spec.tvcf.fo.dat    ,             谱函数输出文件
      spec.tvcf.ft.dat    ,             关联函数输出文件
      spec.tvcf.log       ,             log 文件
      spec.tvcf.spec.dat  ,             光谱文件


1) 计算完成后先确认关联函数是否收敛，将 spec.tvcf.ft.dat 的前两列画图，若随着积分时间的增加，纵坐标的值基本为 0 且呈直线，则表示关联函数已经收敛。



2) 确认关联函数收敛后，根据光谱文件 spec.tvcf.spec.dat，选取所需数据画出 相关的吸收光谱和发射光谱:


3) 辐射速率 kr 可在 spec.tvcf.log 文件末端读取。如下图所示，第一个数值和第 二个数值都表示辐射速率，单位分别是 au 和 s-1，第三个数值表示寿命。计算得 到 azulene 分子的辐射速率 kr 为 2.72281554×105s-1。





4. 非辐射速率
------------

本部分计算文件在 azulene/kic/目录下。

计算内转换过程不仅需要分子基态 S0 与激发态 S1 的构型优化结果、频率计算结果，还需要包含与**非绝热耦合矩阵元相关的 azulene-nacme.log 文件**。非绝热 耦合计算时使用的计算方法、泛函等尽量与构型优化时保持一致。

a. 非绝热耦合矩阵元:
++++++++++++++++++

本部分计算文件在 azulene/kic/nacme/目录下。

在 S0 最稳定构型下设置关键词为:

.. code-block:: bash

	#p td B3lyp/6-31G(d) prop=(fitcharge,field) iop(6/22=-4, 6/29=1, 6/30=0, 6/17=2) nosymm


b. 振动分析(EVC):
++++++++++++++++++

本部分计算文件在相关算例 azulene/kic/evc/目录下。

收集基态、激发态计算结果文件，包括日志文件 (azulene-s0.log 和 azulene-s1.log)和格式化的 Checkpoint 文件(azulene-s0.fchk 和 azulene-s1.fchk)，注意需保证振动结果无虚频。此外，还有 非绝热耦合矩阵元相关的 azulene-nacme.log 文件。将这些文件都放在同一个目录中，编写 EVC 振动分析的输入文件 momap.inp

.. code-block:: bash

	do_evc          = 1                      #1 表示开启dushin计算，0 表示关闭

	&evc
	  ffreq(1)      = "azulene-s0.log"       #基态结果的日志文件
	  ffreq(2)      = "azulene-s1.log"       #激发态结果的日志文件
	  fnacme        = "azulene-nacme.log"    #非绝热耦合文件

	/


执行以下命令运行 EVC 振动分析程序:

	``momap –input momap.inp –nodefile nodefile``

程序正常结束后，得到下一步计算的输入文件 evc.cart.dat 和 evc.cart.nac。


c. 非辐射速率输入文件 momap.inp:
+++++++++++++++++++++++++++++


.. code-block:: bash

	do_ic_tvcf_ft   = 1                   #1 表示开启计算内转换关联函数
	do_ic_tvcf_spec = 1	                #1 表示开启计算内转换光谱

	&spec_tvcf                              #描述计算内容
	  DUSHIN        True                    #是否考虑 Duschinsky 转动(t 开启，f 关闭)
	  Temp          300                     #温度
	  tmax          1000                    #积分时间
	  dt            1                       #积分步长
	  Ead           0.07509                 #绝热激发能
	  DSFile        "evc.cart.dat"          #定义读取的 evc 文件名
	  CoulFile      "evc.cart.nac"          #定义读取的 nacme 文件名
	  Emax          0.3 au                  #定义光谱频率范围上限
	  dE            0.00001                 #定义输出能量间隔
	  logFile       "spec.tvcf.log"         #定义输出 log 文件名
	  FtFile        "spec.tvcf.ft.dat"      #定义输出的关联函数文件名
	  FoFile        "spec.tvcf.fo.dat"      #谱函数输出文件
	/

d. 计算结果解读:
+++++++++++++++++++

运行结束后会得到结果文件与相应解读与辐射速率结果类似。
