"""Documentation about the EVC module."""


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
        “s0.log” (Default)

    Example:
        >>> &evc
        >>>     ffreq(1) = "azulene-s0.log"
        >>>     ffreq(2) = "azulene-s1.log"        
    """

def fnacme(str):
    """定义读取的非绝热耦合矩阵元文件，可由Gaussian等软件计算得到，用于内转换计算

    Args:
        “nacme.log” (Default)

    Example:
        >>> &evc
        >>>     fnacme = "azulene-nacme.log"      
    """

def ftdipd(str):
    """定义读取的numfreq计算文件，用于Herzberg-Teller 效应的计算

    Args:
        “numfreq-es.out” (Default)

    Example:
        >>> &evc
        >>>     fnacme = "numfreq-es.out"      
    """

def sort_mode(int):
    """用于Herzberg-Teller效应的计算

    Args:
        1 (Default): 0

    Example:
        >>> &evc
        >>>     sort_mode      = 1      
    """
