import numpy as np
import scipy.misc as misc


def func(n_int):
    if n_int == 0:
        return 1
    n = np.float128(n_int)
    s = np.float128(np.sqrt(2 * np.pi * n))
    e = np.float128((n / np.e) ** n)
    return np.float128(s * e)


def test():
    for i in range(0, 1000):
        m = misc.factorial(i, False)
        f = func(i)
        print(i, m, f)