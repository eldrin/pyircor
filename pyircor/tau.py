"""
Kendall `\tau` Rank Correlation Coefficients

`\tau` is the rank correlation by Kendall, where neither vector can contain tied
items. `\tau_a` and `tau_b` are the versions developed to cope with ties under the
scenarios of accuracy and agreement, respectively. See the references for details.

.. [1] M.G. Kendall (1970). Rank Correlation Methods. Charles Griffin & Company Limited.
"""

import numba as nb
import numpy as np
from .check import check, check_a, check_b


def tau(x, y):
    """Kendall :math:`\tau` Rank Correlation Coefficients

    Inputs:
        x (Iterable of numeric): input vector
        y (Iterable of numeric): another vector for comparison
    
    Returns:
        float: the correlation coefficient.
    """
    x, y = check(x, y)
    return _tau(x, y)


@nb.njit('f8(f8[:], f8[:])')
def _tau(x, y):
    """Helper function for faster computation"""
    n = len(x)
    numerator = 0
    for i in range(n-1):
        for j in range(i+1, n):
            sx = np.sign(x[i] - x[j])
            sy = np.sign(y[i] - y[j])
            numerator += sx * sy
    nn = n * (n-1) / 2
    return numerator / nn


def tau_a(x, y):
    """Kendall :math:`\tau_a` Rank Correlation Coefficients

    Inputs:
        x (Iterable of numeric): true scores
        y (Iterable of numeric): estimated scores for comparison
    
    Returns:
        float: the correlation coefficient.
    """
    x, y = check_a(x, y)
    return _tau(x, y)


def tau_b(x, y):
    """Kendall :math:`\tau_b` Rank Correlation Coefficients

    Inputs:
        x (Iterable of numeric): input vector
        y (Iterable of numeric): another vector for comparison
    
    Returns:
        float: the correlation coefficient.
    """
    x, y = check_b(x, y)
    return _tau_b(x, y)


@nb.njit('f8(f8[:], f8[:])')
def _tau_b(x, y):
    """Helper function for faster computation"""
    n = len(x)
    numerator = 0
    tx = ty = 0
    for i in range(n-1):
        for j in range(i+1, n):
            sx = np.sign(x[i] - x[j])
            sy = np.sign(y[i] - y[j])
            numerator += sx * sy
            if sx == 0:
                tx += 1
            if sy == 0:
                ty += 1

    nn = n * (n-1) / 2
    return numerator / (nn - tx)**.5 / (nn - ty)**.5