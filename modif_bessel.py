import numpy as np
import scipy.integrate as integrate
import gamma
import scipy.misc as misc
import matplotlib.pyplot as plt


def summ_func(v, z, k):
    numerator = np.float128((0.25 * (z ** 2)) ** np.float128(k))
    f = np.float128(misc.factorial(k, True))
    g = np.float128(gamma.func(v + np.float128(k) + 1))
    denominator = np.float128(f * g)
    ret_val = np.float128(numerator / denominator)
    return np.float128(ret_val)


def getsumm(v, z):

    summ = np.float128(0.0)
    for k in range(0, 100):
        summ += summ_func(v, z, k)
    return np.float128(summ)


def func(v, z):
    k = np.float128((0.5 * z) ** v)
    summ = getsumm(v, z)
    return np.float128(k * summ)


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
