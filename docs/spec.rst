
发光部分
*******

“发光部分”分别以荧光和磷光的计算为例，详细介绍了分子的量化计算、 EVC(Electron-Vibration Coupling)振动分析、吸收光谱、辐射光谱、辐射速率、 内转换速率、系间窜越速率的计算过程。另外，本文还详细介绍了态求和方法和 Herzberg-Teller 效应的计算过程。
 

荧光
===
吸收光谱、荧光光谱以及辐射速率的计算流程以 azulene 为例，算例数据位于 momap/example/azulene/目录下。


1. 量化计算
----------


a. 基态构型优化与频率计算


本算例部分计算文件在 azulene/gaussian/目录下。Gaussian 使用方法详见 Gaussian 手册。


.. code-block:: bash

	#!/bin/sh

 	%chk =azulene-s1.chk 
 	%mem =1GB
	%nprocs =2
	#p td opt Freq B3lyp/6-31G(d)
	azulene-s1 optimization
	0 1
	C 2.01378700 -1.48849800 -0.11795300
	C 2.28995100  0.95357400 -2.15418400
	C 1.39185800  0.00000000  0.00000000
	C 0.78413700  0.00000000  0.00000000




.. seealso::

	The Examples section contains a large number of input examples.





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









b. 激发态构型优化与频率计算

本部分计算文件在 azulene/gaussian/目录下。
基态 S0 构型优化完成后，使用 S0 优化后的构型作为激发态 S1 的初始构型， 用来优化激发态和计算激发态频率。











使用 formchk 命令转化二进制的 checkpoint 文件为文本文件:

formchk azulene-s1.chk

运行结束后生成文件 azulene-s1.fchk。azulene-s1.flog 和 azulene-s1.fchk 这两 个文件将用于下一步的振动分析。




2. 振动分析
----------

本部分计算文件在 azulene/evc/目录下。




3. 辐射速率
----------