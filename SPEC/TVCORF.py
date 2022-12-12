"""Documentation about the MOMAP module."""

def do_ic_tvcf_ft(int):
    """表示开启计算荧光关联函数, 1表示开启，0表示关闭

    Args:
        1 (Default): 0

    Example:
        >>>     do_spec_tvcf_ft      = 1      
    """

def do_spec_tvcf_spec(int):
    """表示开启计算荧光光谱, 1表示开启，0表示关闭

    Args:
        1 (Default): 0

    Example:
        >>>     do_spec_tvcf_ft      = 1      
    """

def DUSHIN(logic):
    """是否开启 Duschinsky t表示开启，f表示关闭

    Args:
        .t. (Default): .f. 

    Example:
        >>> &spec_tvcf
        >>>     DUSHIN      = .t.        
    """

def HERZ(logic):
    """是否开启 Herzberg-Teller 效应的计算

    Args:
        .f. (Default): .t. 

    Example:
        >>> &spec_tvcf
        >>>     HERZ      = .f.        
    """

def Ead(float):
    """ 绝热激发能

    Args:
        0.05 (Default)
 

    Example:
        >>> &spec_tvcf
        >>>     Ead      = 0.075091878 au    
    """

def EDMA(float):
    """ 吸收跃迁偶极矩

    Args:
        0.05 (Default)
 

    Example:
        >>> &spec_tvcf
        >>>     EDMA      = 0.92694 debye   
    """

def EDME(float):
    """ 发射跃迁偶极矩

    Args:
        0.05 (Default)
 

    Example:
        >>> &spec_tvcf
        >>>     EDME      = 0.64751 debye   
    """

def Temp(float):
    """ 定义温度

    Args:
        300 (Default)
 

    Example:
        >>> &spec_tvcf
        >>>     Temp      = 300 K    
    """

def tmax(float):
    """ 积分时间

    Args:
        1000 (Default)
 

    Example:
        >>> &spec_tvcf
        >>>     tmax      = 1000 fs    
    """

def dt(float):
    """ 积分步长

    Args:
        0.01 (Default)
 

    Example:
        >>> &spec_tvcf
        >>>     dt      = 0.01 fs    
    """


def Emax(float):
    """ 定义光谱频率范围上限

    Args:
        0.3 (Default)
 

    Example:
        >>> &spec_tvcf
        >>>     Emax      = 0.3 au  
    """

def dE(float):
    """ 定义输出能量间隔

    Args:
        0.00001 (Default)
 

    Example:
        >>> &spec_tvcf
        >>>     dE      = 0.00001 au   
    """

def FreqScale(float):
    """ 频率缩放因子

    Args:
        1.0 (Default)
 

    Example:
        >>> &spec_tvcf
        >>>     FreqScale      = 1.0  
    """


def DSFile(str):
    """定义读取的 evc 文件名

    Args:
        "evc.cart.dat" (Default)

    Example:
        >>> &spec_tvcf
        >>>     DSFile = "evc.cart.dat"      
    """


def logFile(str):
    """定义输出 log 文件名

    Args:
        "spec.tvcf.log" (Default)

    Example:
        >>> &spec_tvcf
        >>>     logFile = "spec.tvcf.log"      
    """


def FtFile(str):
    """定义输出的关联函数文件名

    Args:
        "spec.tvcf.ft.dat" (Default)

    Example:
        >>> &spec_tvcf
        >>>     FtFile = "spec.tvcf.ft.dat"      
    """


def FoFile(str):
    """谱函数输出文件

    Args:
        "spec.tvcf.fo.dat" (Default)

    Example:
        >>> &spec_tvcf
        >>>     FoFile = "spec.tvcf.fo.dat"      
    """


def FoSFile(str):
    """归一化的光谱输出文件

    Args:
        "spec.tvcf.spec.dat" (Default)

    Example:
        >>> &spec_tvcf
        >>>     FoSFile = "spec.tvcf.spec.dat"      
    """



