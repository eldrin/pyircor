"""
AP Rank Correlation Coefficients

`tauap` is the AP rank correlation coefficient by Yilmaz et al., where neither vector can
contain tied items. `tauap_a` and `tauap_b` are the versions developed by Urbano and
Marrero to cope with ties under the scenarios of accuracy and agreement, respectively. See the
references for details.

Note that the sorting order is decreasing by default, as should be for instance if the scores
represent the effectiveness of systems. When the sorting order is ascending, as is for instance when the vectors represent ranks, the parameter
`decreasing` must be set to `False`

.. [1] E. Yilmaz, J.A. Aslam and S. Pobertson (2008). A New Rank Correlation Coefficient for
    Information Retrieval. ACM SIGIR

.. [2] J. Urbano and M. Marrero (2017). The Treatment of Ties in AP Correlation. ACM ICTIR.
"""

import numpy as np
from scipy import stats
import numba as nb

from .check import check_inputs


@check_inputs('default')
def tauap(x, y, decreasing=True):
    """AP Rank Correlation Coefficient

    Inputs:
        x (Iterable of numeric): input vector
        y (Iterable of numeric): another vector for comparison
    
    Returns:
        float: the correlation coefficient.   
    """
    rx = stats.rankdata(x)
    ry = stats.rankdata(y)
    return _tauap(x, y, rx, ry)
        

@nb.njit('f8(f8[:], f8[:], f8[:], f8[:])')
def _tauap(x, y, rx, ry):
    """Helper function for faster computation"""
    n = len(rx)
    numerator = 0
    for i in range(n-1):
        for j in range(i+1, n):
            sx = np.sign(x[i] - x[j])
            sy = np.sign(y[i] - y[j])
            if sx == sy:
                # since we don't traverse in sored order, divide by the max rank
                numerator += 1 / (max(ry[i], ry[j]) - 1)
    return (2 * numerator / (n-1)) - 1


@check_inputs('a')
def tauap_a(x, y, decreasing=True):
    """AP-a Rank Correlation Coefficients

    Inputs:
        x (Iterable of numeric): true scores
        y (Iterable of numeric): estimated scores for comparison
    
    Returns:
        float: the correlation coefficient.
    """
    rx = stats.rankdata(x)
    ry = stats.rankdata(y, 'ordinal')  # ties.method='first'
    p = stats.rankdata(y, 'min') - 1
    t = np.bincount(p)[p]  # uses large memory to speed up
    return _tauap_a(rx, ry, p, t)


@nb.njit('f8(f8[:], i8[:], i8[:], i8[:])')
def _tauap_a(rx, ry, p, t):
    """
    """
    n = len(rx)
    c_all = 0
    for i in range(len(p)):
        if p[i] == 0:
            continue
        
        c_above = 0
        for j in range(len(p)):
            if p[j] >= p[i]:
                continue

            sx = np.sign(rx[i] - rx[j])
            sy = np.sign(ry[i] - ry[j])

            if sx == sy:
                c_above += 1
        s_above = np.sum( 1 / (p[i] + np.arange(t[i])) / t[i] )

        c_all += c_above * s_above
    
    # term II: concordants within the group across permutations
    for i in range(len(p)):
        c_within = 0
        for k in range(t[i] - 1):
            c_within += (k+1) / (p[i] + k + 1)
        c_within = (c_within / 2 / t[i])
        c_all += c_within

    return (2 / (n - 1) * c_all) - 1


@check_inputs('b')
def tauap_a_sign(x, y, decreasing=True):
    """AP-a Rank Correlation Coefficients

    this version allows ties in reference signal `x`

    Inputs:
        x (Iterable of numeric): true scores
        y (Iterable of numeric): estimated scores for comparison
    
    Returns:
        float: the correlation coefficient.
    """
    rx = stats.rankdata(x)
    ry = stats.rankdata(y, 'ordinal')  # ties.method='first'
    p = stats.rankdata(y, 'min') - 1
    t = np.bincount(p)[p]  # uses large memory to speed up
    return _tauap_a(rx, ry, p, t)


@nb.njit('f8(f8[:], i8[:], i8[:], i8[:])')
def _tauap_a_sign(rx, ry, p, t):
    """
    """
    n = len(rx)
    c_all = 0
    for i in range(len(p)):
        if p[i] == 0:
            continue
        
        c_above = 0
        for j in range(len(p)):
            if p[j] >= p[i]:
                continue

            sx = np.sign(rx[i] - rx[j])
            sy = np.sign(ry[i] - ry[j])

            c_above += sx * sy
        s_above = np.sum( 1 / (p[i] + np.arange(t[i])) / t[i] )
        c_all += c_above * s_above
    
    return c_all / (n-1)


@check_inputs('b')
def tauap_b(x, y, decreasing=True):
    """AP-b Rank Correlation Coefficient

    Inputs:
        x (Iterable of numeric): input vector
        y (Iterable of numeric): another vector for comparison
    
    Returns:
        float: the correlation coefficient.   
    """
    return (tauap_b_ties(x, y) + tauap_b_ties(y, x)) / 2


def tauap_b_ties(x, y, decreasing=True):
    """Helper function"""
    rx = stats.rankdata(x)
    ry = stats.rankdata(y, 'ordinal')  # ties.method = 'first'
    p = stats.rankdata(y, 'min') - 1 # ties.method = 'min'
    return _tauap_b_ties(rx, ry, p)


@nb.njit('f8(f8[:], i8[:], i8[:])', error_model='numpy')
def _tauap_b_ties(rx, ry, p):
    """Helper function for faster computation"""
    c_all = 0
    n_not_top = 0
    for i in range(len(p)):
        # ignore the first items group
        if p[i] == 0:
            continue
        n_not_top += 1
        
        # count concordants above the pivot's tie group
        c_above = 0
        for j in range(len(p)):
            if p[j] >= p[i]:
                continue
    
            sx = np.sign(rx[i] - rx[j])
            sy = np.sign(ry[i] - ry[j])

            if sx == sy:
                c_above += 1
        c_all += c_above / p[i]  # divide by p-1 instead of i-1
    return 2 / n_not_top * c_all - 1