"""A typical MOMAP control file momap.inp can be as follows:



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


"""


def do_evc(int):
    """是否开启dushin计算, 1表示开启，0表示关闭

    Args:
        1 (Default): 0 

    Example:
        >>>     do_evc      =  1      
    """

def ffreq(str):
    """定义读取的基态或激发态结果的日志文件，可由Gaussian等软件计算得到

    Args:
        “s0-freq.log” (Default)

    Example:
        >>> &evc
        >>>     ffreq(1) = "s0-freq.log"
        >>>     ffreq(2) = "s1-freq.log"        
    """

def fnacme(str):
    """定义读取的非绝热耦合矩阵元文件，可由Gaussian等软件计算得到，用于内转换计算

    Args:
        “nacme.log” (Default)

    Example:
        >>> &evc
        >>>     fnacme = "nacme.log"      
    """

def ftdipd(str):
    """定义读取的DIP输出文件，用于Herzberg-Teller 效应的计算

    Args:
        “numfreq-es.out” (Default)

    Example:
        >>> &evc
        >>>     fnacme = "numfreq-es.out"      
    """

def sort_mode(int):
    """用于Herzberg-Teller效应的计算

    Args:
        0 (Default): 1

    Example:
        >>> &evc
        >>>     sort_mode      = 0  
    """
