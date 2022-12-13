"""Documentation about the MOMAP module."""

def do_transport_prepare(int):
    """是否生成预备文件, 1表示开启，0表示关闭

    Args:
        1 (Default): 0

    Example:
        >>> &transport
        >>>     do_transport_prepare      = 1      
    """

def do_transport_submit_HL_job(int):
    """是否开启计算转移积分, 1表示开启，0表示关闭

    Args:
        1 (Default): 0

    Example:
        >>> &transport
        >>>     do_transport_submit_HL_job      = 1      
    """

def do_transport_get_transferintegral(int):
    """计算计算转移积分, 1表示开启，0表示关闭

    Args:
        1 (Default): 0

    Example:
        >>> &transport
        >>>     do_transport_get_transferintegral      = 1      
    """

def do_transport_submit_RE_job(int):
    """计算重整能, 1表示开启，0表示关闭

    Args:
        1 (Default): 0

    Example:
        >>> &transport
        >>>     do_transport_submit_RE_job      = 1      
    """


def do_transport_get_re_evc(int):
    """使用 evc 程序分析重整能, 1表示开启，0表示关闭

    Args:
        1 (Default): 0

    Example:
        >>> &transport
        >>>     do_transport_get_re_evc      = 1      
    """

def do_transport_run_MC(int):
    """Monte_Carlo 模拟, 1表示开启，0表示关闭

    Args:
        1 (Default): 0

    Example:
        >>> &transport
        >>>     do_transport_run_MC      = 1      
    """


def do_transport_get_mob_MC(int):
    """计算迁移率, 1表示开启，0表示关闭

    Args:
        1 (Default): 0

    Example:
        >>> &transport
        >>>     do_transport_get_mob_MC      = 1      
    """



def do_transport_run_MC_temp(int):
    """不同温度下的Monte_Carlo 模拟, 1表示开启，0表示关闭

    Args:
        0 (Default): 1

    Example:
        >>> &transport
        >>>     do_transport_run_MC_temp      = 0      
    """

def do_transport_get_mob_MC_temp(int):
    """计算不同温度下的迁移率, 1表示开启，0表示关闭

    Args:
        0 (Default): 1

    Example:
        >>> &transport
        >>>     do_transport_get_mob_MC_temp      = 0      
    """

def do_transport_run_ME(int):
    """ME 方面模拟, 1表示开启，0表示关闭

    Args:
        1 (Default): 0

    Example:
        >>> &transport
        >>>     do_transport_run_ME      = 0   
    """


def do_transport_get_mob_ME(int):
    """计算迁移率, 1表示开启，0表示关闭

    Args:
        0 (Default): 1

    Example:
        >>> &transport
        >>>     do_transport_get_mob_ME      = 0     
    """


def do_transport_run_ME_temp(int):
    """不同温度下的 ME 模拟, 1表示开启，0表示关闭

    Args:
        0 (Default): 1

    Example:
        >>> &transport
        >>>     do_transport_run_ME_temp      = 0     
    """

def do_transport_get_mob_ME_temp(int):
    """计算不同温度下的迁移率, 1表示开启，0表示关闭

    Args:
        0 (Default): 1

    Example:
        >>> &transport
        >>>     do_transport_get_mob_ME_temp      = 0      
    """

def do_transport_gather_momap_data(int):
    """收集打印电荷疏运计算的相关数据, 1表示开启，0表示关闭

    Args:
        1 (Default): 0

    Example:
        >>> &transport
        >>>     do_transport_gather_momap_data      = 1      
    """

def crystal(str):
    """定义晶体文件

    Args:
        crystal.cif (Default)

    Example:
        >>> &transport
        >>>     crystal = naphthalene.cif      
    """

def lat_cutoff(float):
    """计算相邻转移积分的截断半径(单位:Å)，这意味着如果两个分子的最近原子距离小于 lat_cutoff，则考虑计算它们之间的转移积分。

    Args:
        4 (Default)

    Example:
        >>> &transport
        >>>     lat_cutoff = 4     
    """

def ratetype(str):
    """定义电子空穴迁移速率计算方法，可选经典marcus方法或者量子修正的quantum方法

    Args:
        quantum (Default)：marcus

    Example:
        >>> &transport
        >>>     ratetype = quantum     
    """

def temp(float):
    """定义模拟温度

    Args:
        300 (Default)

    Example:
        >>> &transport
        >>>     temp = 200     
    """


def start_temp(float):
    """计算不同温度下的电荷迁移率时，定义模拟初始温度

    Args:
        200 (Default)

    Example:
        >>> &transport
        >>>     start_temp = 200     
    """

def end_temp(float):
    """计算不同温度下的电荷迁移率时，定义模拟最终温度

    Args:
        300 (Default)

    Example:
        >>> &transport
        >>>     end_temp = 300     
    """

def delta_temp(float):
    """定义模拟温度间隔，例如，若 Start_Temp，End_Temp 和 delta_Temp 分别为 200，300，50，那么将进行 200K，250K，300 K 下的蒙特卡罗模拟

    Args:
        50 (Default)

    Example:
        >>> &transport
        >>>     delta_temp = 50     
    """

def nsimu(int):
    """定义模拟次数

    Args:
        2000 (Default)

    Example:
        >>> &transport
        >>>     nsimu = 2000
    """

def tsimu(int):
    """定义总模拟时间（in ns）

    Args:
        1000 (Default)

    Example:
        >>> &transport
        >>>     tsimu = 1000
    """

def tsnap(int):
    """定义记录输出文件中的载流子位置的时间间隔

    Args:
        5 (Default)

    Example:
        >>> &transport
        >>>     tsnap = 5
    """
