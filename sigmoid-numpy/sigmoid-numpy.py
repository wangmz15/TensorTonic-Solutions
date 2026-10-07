import numpy as np

def sigmoid(x: list | float) -> np.ndarray | float:
    """
    Returns the sigmoid value for a scalar or each element of a list.
    """
    is_scalar = isinstance(x, (int, float))
    arr = np.array(x, dtype=float)
    res = 1 / (1 + np.exp(-arr))
    return float(res) if is_scalar else res