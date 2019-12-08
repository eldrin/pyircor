import numba as nb
import numpy as np
from .check import check, check_a, check_b


def tau(x, y):
    """
    """
    x, y = check(x, y)
    return _tau(x, y)


@nb.njit('f8(f8[:], f8[:])')
def _tau(x, y):
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
    """
    """
    x, y = check_a(x, y)
    return _tau(x, y)


def tau_b(x, y):
    """
    """
    x, y = check_b(x, y)
    return _tau_b(x, y)


@nb.njit('f8(f8[:], f8[:])')
def _tau_b(x, y):
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