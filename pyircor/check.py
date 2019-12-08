import numpy as np
from collections import Iterable


def is_numeric(obj):
    # from https://stackoverflow.com/a/500908
    attrs = ['__add__', '__sub__', '__mul__', '__truediv__', '__pow__']
    return all(hasattr(obj, attr) for attr in attrs)


def _check_types(x, arg_str):
    bad = False
    if isinstance(x, Iterable):
        x = np.array(x)
        if is_numeric(x) and x.size > 1:
            pass
        else:
            bad = True
    else:
        bad = True

    if bad:
        raise ValueError(
            '[ERROR] input {} must be a numeric vector'.format(arg_str)
        )
    return x


def check_types(x, y):
    x = _check_types(x, 'x')
    y = _check_types(y, 'y')
    if len(x) != len(y):
        raise ValueError('[ERROR] x and y must be of the same length')
    return x, y


def has_ties(x):
    return len(x) != len(set(x))


def check(x, y):
    x, y = check_types(x, y)
    if has_ties(x):
        raise ValueError('[ERROR] x contains ties')
    if has_ties(y):
        raise ValueError('[ERROR] y contains ties.')
    return x, y


def check_a(x, y):
    x, y = check_types(x, y)
    if has_ties(x):
        raise ValueError('[ERROR] x contains ties')
    return x, y


def check_b(x, y):
    return check_types(x, y)


def check_inputs(check_type='default'):
    def real_check_inputs(func):
        def wrapper(x, y, decreasing=True, *args, **kwargs):
            if check_type == 'default':
                x, y = check(x, y)
            elif check_type == 'a':
                x, y = check_a(x, y)
            elif check_type == 'b':
                x, y = check_b(x, y)

            if decreasing:
                return func(-x, -y, decreasing=False, *args, **kwargs)
            else:
                return func(x, y, *args, **kwargs)
        return wrapper
    return real_check_inputs
