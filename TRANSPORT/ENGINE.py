"""Documentation about the MOMAP module."""

def compute_engine(int):
    """定义使用的计算引擎，1 = Gaussian, 2 = ORCA, 3 = QCHEM， 4 = BDF

    Args:
        1 (Default): 0

    Example:
        >>> &transport
        >>>     compute_engine      = 1      
    """


def qc_exe(str):
    """g09/g16 or fullpath/orca or qchem

    Args:
        g09 (Default)

    Example:
        >>> &transport
        >>>     qc_exe = g09      
    """



