

def do_spec_sums(int):
    """是否开启计算辐射关联函数, 1表示开启，0表示关闭

    Args:
        1 (Default): 0

    Example:
        >>>     do_spec_sums      = 1      
    """

def Ead(float):
    """ 绝热激发能,可由Gaussian等软件计算得到

    Args:
        0.05 (Default)
 

    Example:
        >>> &spec_sums
        >>>     Ead      = 0.075091878 au    
    """

def dipole_abs(float):
    """ 吸收跃迁偶极矩，可由Gaussian等软件计算得到

    Args:
        0.05 (Default)
 

    Example:
        >>> &spec_sums
        >>>     dipole_abs      = 0.92694 debye   
    """

def dipole_emi(float):
    """ 发射跃迁偶极矩，可由Gaussian等软件计算得到

    Args:
        0.05 (Default)
 

    Example:
        >>> &spec_sums
        >>>     dipole_emi      = 0.64751 debye   
    """


def FC_eps_abs(float):
    """ 定义Franck-Condon 因子阈值(吸收)

    Args:
        0.1 (Default)
 

    Example:
        >>> &spec_sums
        >>>     FC_eps_abs      = 0.1   
    """

def FC_eps_emi(float):
    """ 定义Franck-Condon 因子阈值(辐射)

    Args:
        0.1 (Default)
 

    Example:
        >>> &spec_sums
        >>>     FC_eps_emi      = 0.1   
    """

def FC_eps_ic(float):
    """ 定义Franck-Condon 因子阈值(内转换)

    Args:
        0.1 (Default)
 

    Example:
        >>> &spec_sums
        >>>     FC_eps_ic      = 0.1   
    """

def if_cal_ic(logic):
    """是否做内转换通道分析

    Args:
        .f. (Default): .t. 

    Example:
        >>> &spec_sums
        >>>     if_cal_ic      = .f.        
    """

def maxvib(int):
    """ 定义最大振动量子数

    Args:
         10 (Default)
 

    Example:
        >>> &spec_sums
        >>>     maxvib      = 10 
    """

def promode(int):
    """ 定义提升模式(内转换通道分析)

    Args:
         24 (Default)
 

    Example:
        >>> &spec_sums
        >>>     promode      = 24  
    """

def FWHM(float):
    """ 定义展宽因子(半高全宽)

    Args:
        500 (Default)
 

    Example:
        >>> &spec_sums
        >>>     FWHM      = 500 cm-1 
    """

def Seps(float):
    """ 定义黄昆因子阈值

    Args:
        0.00001 (Default)
 

    Example:
        >>> &spec_sums
        >>>     Seps      = 0.00001  
    """

def FreqScale(float):
    """ 定义频率缩放因子

    Args:
        1.0 (Default)
 

    Example:
        >>> &spec_sums
        >>>     FreqScale      = 1.0  
    """


def DSFile(str):
    """定义读取的 evc 文件名

    Args:
        "evc.cart.dat" (Default)

    Example:
        >>> &spec_sums
        >>>     DSFile = "evc.cart.dat"      
    """


def flog(str):
    """定义输出 log 文件名

    Args:
        "spec.sums.log" (Default)

    Example:
        >>> &spec_sums
        >>>     flog = "spec.sums.log"      
    """



"""A typical **MOMAP** control file momap.inp can be as follows:



.. code-block:: bash


    do_evc                 = 1
    do_spec_tvcf_ft        = 0
    do_spec_tvcf_spec      = 0
    do_ic_tvcf_ft          = 1
    do_ic_tvcf_spec        = 1
    do_isc_tvcf_ft         = 0
    do_isc_tvcf_spec       = 0
    do_spec_sums           = 0  

    &evc 
    ...
    /   

    &spec_tvcf
    ...
    /   

    &ic_tvcf 
    ...
    /   

    &isc_tvcf 
    ...
    /   

    &spec_sums
    ...
    /



The typical **evc** control with momap.inp can be as follows:


.. code-block:: bash

    do_evc          = 1                   #1 表示开启dushin计算，0 表示关闭

    &evc
      ffreq(1)      = "s0-freq.log"       #基态结果的日志文件
      ffreq(2)      = "s1-freq.log"       #激发态结果的日志文件
    /

or


.. code-block:: bash

    do_evc          = 1                   #1 表示开启dushin计算，0 表示关闭

    &evc
      ffreq(1)      = "s0-freq.log"       #基态结果的日志文件
      ffreq(2)      = "s1-freq.log"       #激发态结果的日志文件
      fnacme        = "nacme.log"         #nacme计算输出文件
      sort_mode     = 1                   #模式
    /

or


.. code-block:: bash

    do_evc          = 1                   #1 表示开启dushin计算，0 表示关闭

    &evc
      ffreq(1)      = "s0-freq.log"       #基态结果的日志文件
      ffreq(2)      = "s1-freq.log"       #激发态结果的日志文件
      ftdipd        = "numfreq-es.out"    #dip计算输出文件
      sort_mode     = 1                   #模式
    /


or


.. code-block:: bash

    do_evc          = 1                   #1 表示开启dushin计算，0 表示关闭

    &evc
      ffreq(1)      = "s0-freq.log"       #基态结果的日志文件
      ffreq(2)      = "s1-freq.log"       #激发态结果的日志文件
      ftdipd        = "numfreq-es.out"    #dip计算输出文件
      sort_mode     = 1                   #模式
    /

or


.. code-block:: bash

    do_evc          = 1                   #1 表示开启dushin计算，0 表示关闭

    &evc
      ffreq(1)      = "s0-freq.log"       #基态结果的日志文件
      ffreq(2)      = "s1-freq.log"       #激发态结果的日志文件
      ftdipd        = "numfreq-es.out"    #dip计算输出文件
      sort_mode     = 1                   #模式
    /



"""