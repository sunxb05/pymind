
发光部分
*******

“发光部分”分别以荧光和磷光的计算为例，详细介绍了分子的量化计算、 EVC(Electron-Vibration Coupling)振动分析、吸收光谱、辐射光谱、辐射速率、内转换速率、系间窜越速率的计算过程。另外，本文还详细介绍了态求和方法和 Herzberg-Teller 效应的计算过程。
 

荧光
======
吸收光谱、荧光光谱以及辐射速率的计算流程以 azulene 为例，算例数据位于 momap/example/azulene/目录下。


1. 量化计算
-----------


a. 基态构型优化与频率计算
++++++++++++++++++++++


本算例部分计算文件在 azulene/gaussian/目录下。Gaussian 使用方法详见 Gaussian 手册。
以下为使用Gaussian进行基态构型优化与频率计算的输入文件的例子：

.. code-block:: bash

	%chk=azulene-s0.chk         #输出 chk 文件
	%mem=4GB                    #内存大小
	%nprocl=1                   #使用节点数
	%nprocs=16                  #每个节点上的并行的核数
	#p opt freq B3LYP/6-31G     #基于DFT方法/B3LYP 泛函/6-31G(d)基组对分子基态构型进行优化，然后计算优化后分子构型的频率

	azulene-s0 optimization	    #标题行

	0 1                         #净电荷数为 0，自选多重度为 1
	 C                  2.01378743   -1.48849852    0.00000000
	 C                  2.28995141   -0.11795315    0.00000000
	 C                  1.39185815    0.95357383    0.00000000
	 C                  0.78413689   -2.15418449    0.00000000
	 C                  0.00000000    0.93285810    0.00000000
	 C                 -0.50398383   -1.61065958    0.00000000
	 C                 -0.89316505   -0.27406276    0.00000000
	 H                  2.88919252   -2.13621797    0.00000000
	 H                  3.34387207    0.15083266    0.00000000
	 H                  1.84191311    1.94635990    0.00000000
	 H                  0.83658347   -3.24058384    0.00000000
	 H                 -1.32037398   -2.33298523    0.00000000
	 C                 -0.84567310    2.05536637    0.00000000
	 H                 -0.51364908    3.08694089    0.00000000
	 C                 -2.17758707    1.61062710    0.00000000
	 H                 -3.04994479    2.25593917    0.00000000
	 C                 -2.21339978    0.20656494    0.00000000
	 H                 -3.10314368   -0.41207657    0.00000000



计算结束后得到 azulene-s0.chk 和 azulene-s0.log 输出文件。
使用以下指令对二进制的 checkpoint 文件进行转换: 

	``formchk azulene-s0.chk``

运行结束后生成文件 azulene-s0.fchk，azulene-s0.flog 和 azulene-s0.fchk 这两个文件将用于后续的振动分析计算。




b. 激发态构型优化与频率计算
+++++++++++++++++++++++++

本部分计算文件在 azulene/gaussian/目录下。
基态 S0 构型优化完成后，使用 S0 优化后的构型作为激发态 S1 的初始构型， 用来优化激发态和计算激发态频率。


.. code-block:: bash

	%chk=azulene-s1.chk
	%mem=4GB
	%nprocl=1
	%nprocs=16
	#p opt freq td b3lyp/6-31g(d)	#基于TDDFT方法/B3LYP 泛函/6-31G(d)基组对分子激发态构型进行优化，然后计算优化后分子构型的频率

	azulene-s1 optimization	

	0 1
	 C                  2.01378700   -1.48849900    0.00000000
	 C                  2.28995100   -0.11795300    0.00000000
	 C                  1.39185800    0.95357400    0.00000000
	 C                  0.78413700   -2.15418400    0.00000000
	 C                  0.00000000    0.93285800    0.00000000
	 C                 -0.50398400   -1.61066000    0.00000000
	 C                 -0.89316500   -0.27406300    0.00000000
	 H                  2.88919300   -2.13621800    0.00000000
	 H                  3.34387200    0.15083300    0.00000000
	 H                  1.84191300    1.94636000    0.00000000
	 H                  0.83658300   -3.24058400    0.00000000
	 H                 -1.32037400   -2.33298500    0.00000000
	 C                 -0.84567300    2.05536600    0.00000000
	 H                 -0.51364900    3.08694100    0.00000000
	 C                 -2.17758700    1.61062700    0.00000000
	 H                 -3.04994500    2.25593900    0.00000000
	 C                 -2.21340000    0.20656500    0.00000000
	 H                 -3.10314400   -0.41207700    0.00000000




计算结束后得到 azulene-s1.chk 和 azulene-s1.log 输出文件。
使用以下指令对二进制的 checkpoint 文件进行转换: 

	``formchk azulene-s1.chk``

运行结束后生成文件 azulene-s1.fchk，azulene-s1.flog 和 azulene-s1.fchk 这两个文件将用于后续的振动分析计算。




2. 振动分析 
----------

本部分计算文件在 azulene/evc/目录下。


收集以上计算得到的基态和激发态的计算结果文件，包括日志文件 (azulene-s0.log、azulene-s1.log)和格式化的 Checkpoint 文件(azulene-s0.fchk、 azulene-s1.fchk)，注意需保证振动结果无虚频(在频率计算文件中搜索 Frequencies，注意 F 大写，可以找到频率信息)，将这些文件都放在一个文件夹 (evc)中，编写 EVC 振动分析的输入文件 momap.inp:

.. code-block:: bash

	do_evc          = 1                    # 1 表示开启dushin计算，0 表示关闭

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

   	如果不使用队列脚本，可以在 nodefile 里 指定节点名称和核数。例如:需要使用节点名称为 node1 和 node2 的两个节点，

   	每个节点上使用 2 个核。则 nodefile 写为 ::

	    node1 	
	    node1 	
	    node2 	
	    node2





3. 辐射速率
----------










.. important::

   Most options described in this manual should be specified in the Engine block::

    # All keywords should be specified inside the 'Engine' block
      Engine
         Basis
            Type DZP
         End

         XC
            GGA PBE
         End
      EndEngine


You can put more remarks in the input file to be echoed in the standard output file; these will not become part of the job identification:

::

   COMMENT
      text
      ...
   end



New syntax for a few keywords
+++++++++++++++++++++++++++++

In order to adapt to the new (more strict) input format, the syntax of a few keywords had to be changed.


.. csv-table::
   :header: "key in 2017 and before", "key in 2018 and later / comments"


      EField                      , 2020: key 'System%ElectroStaticEmbedding' in
      Geometry                    , 2020: key 'Task' and key 'Properties' in
      Thermo                      , 2020: key 'Thermo' in

Strict parsing of input file
++++++++++++++++++++++++++++

In2018 and later **exact keyword matching** is used, meaning that **keywords abbreviations (or extensions) are not allowed**.
In2017 (and previous versions) the parsing of the input file was *tolerant* and it would allow for abbreviations and extension of keywords.

In the example below, only the first version is allowed in2018 and later, while the second and third version will trigger an input syntax error::

   # This is the proper input syntax:
   SCF
      Converge 1.0E-7
   End






