import numpy as np
from scipy import stats 


def permute_ties(x, decreasing=True):
    """
    """
    if decreasing:
        x = -x
    
    ranks = stats.rankdata(x, 'ordinal')
    groups = stats.rankdata(x, 'min')
    _permute_ties(ranks, groups)


def _permute_ties(ranks, groups, prev=0, l=[]):
    if len(ranks) == 1:
        # only one item remaining. Contatenate and add
        l = np.concatenate([np.array(l), ranks, groups])
    else:
        # work out the next item. Obtain tied items and their ranks
        same_group = np.where(groups == groups[0])[0]
        group_ranks = ranks[same_group]
        # recursively process the res, rotating within the same group
        for i in range(len(same_group)):
            ranks2 = ranks[1:]
            ranks2[same_group[1:] - 1] = group_ranks[-i]
            groups2 = groups[1:]
            prev2 = np.r_[prev, group_ranks[i]]
            l = _permute_ties(ranks2, groups2, prev2, l)
    return l
