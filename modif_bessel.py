import numpy as np
import scipy.integrate as integrate
import gamma
import scipy.misc as misc
import matplotlib.pyplot as plt
import scipy.special as spec

from factorial import func as fact

numb_term = 36
porog = 700


def summ_func(v, z, k, flag=False):
    numerator = np.float128((0.25 * (z ** 2)) ** np.float128(k))
    f = np.float128(fact(k))
    # f = np.float128(misc.factorial(k, False) 
    #g = spec.gamma(v + k + 1)
    g = np.float128(gamma.func(v + np.float128(k) + 1))
    denominator = np.float128(f * g)
    # ret_val = np.float128(numerator / denominator)
    # ret_val = np.float128(numerator / (f * g))
    ret_val = np.float128((numerator / f) * (numerator / g))
    if flag is True:
        print(numerator, f, g, f *g)
    return np.float128(ret_val)


def getsumm(v, z, flag=False):

    summ = np.float128(0.0)
    # -6.62863316177e+23
    for k in range(0, numb_term):
        summ += summ_func(v, z, k, flag)
    if flag is True:
        print('summ = ', summ)
    return np.float128(summ)


def func(v, z, flag=False):

    if z >= porog:
        k = np.float128((0.5 * z) ** v)
        summ = getsumm(v, z)
        modbes = np.float128(k * summ)
        if flag is True:
            print("is my")
    else:
        modbes = np.float128(spec.iv(int(v), float(z)))
        if flag is True:
            print("is scipy")
    return modbes


def plot():
    x = list()
    y = list()
    for z in np.arange(0, 5, 0.1, dtype=np.float128):
        x.append(z)
        f = np.float128(func(5, z))
        y.append(f)

    plt.plot(x, y)
    plt.axis([0, 5, 0, 5])
    plt.grid()
    plt.show()


def test():
    for i in range(0, 800):
        norm = spec.iv(50, i)
        custom = func(50, i)
        print(i, norm, custom, norm - custom)
