"""Documentation about the MOMAP module."""


def DUSHIN(logic):
    """是否开启 Duschinsky 转动效应的计算

    Args:
        .t. (Default): .f. 

    Usage:

        &control
            DUSHIN      = .t.        
    """

def HERZ(logic):
    """是否开启 Herzberg-Teller 效应的计算

    Args:
        .f. (Default): .t. 

    Usage:

        &control
            HERZ      = .f.        
    """

def Temp(float):
    """ 定义温度

    Args:
        298 (Default)

    Usage:

        &control
            Temp      = 298 K    

    Example:
        This function can be called with `Jane Smith` as argument using

        from pymind.my_module import hello
        hello('Jane Smith')   
    """