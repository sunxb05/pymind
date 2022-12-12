"""Documentation about the EVC module."""


def do_evc(int):
    """是否开启dushin计算, 1表示开启，0表示关闭

    Args:
        1 (Default): 0 

    Example:
        >>>     do_evc      =  1      
    """

def ffreq(str):
    """基态或激发态结果的日志文件

    Args:
        “s0.log” (Default)

    Example:
        >>> &evc
        >>>     ffreq(1) = "azulene-s0.log"
        >>>     ffreq(2) = "azulene-s1.log"        
    """

def fnacme(str):
    """非绝热耦合文件

    Args:
        “nacme.log” (Default)

    Example:
        >>> &evc
        >>>     fnacme = "azulene-nacme.log"      
    """