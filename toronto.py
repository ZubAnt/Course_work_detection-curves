import numpy as np
import scipy.stats as stats
import scipy.special as special
import scipy.integrate as integrate
import matplotlib.pyplot as plt

import num_integrate


def integrand(t, m, N, r):
    return (t ** (m - N)) * np.exp(-(t ** 2)) * special.i1(2 * r * t)


def plot_integrand_one_impulse():
    x = list()
    y = list()

    for i in np.arange(0.1, 100, 0.1):
        x.append(i)
        y.append(integrand(i, 1, 0, i / np.sqrt(2)))

    plt.plot(x, y)
    plt.grid()
    plt.title('график подинтеграла функции Торонто (по по инф. техн.)')
    plt.show()


def func(a, m, N, r):
    if N != 0:
        raise ValueError("now N must be equal 0")

    k = 2 * (r ** (N - m + 1)) * np.exp(-(r ** 2))
    integral = integrate.quad(lambda t: integrand(t, m, N, r), 0, a)[0]

    ## Расчет методом трапеций
    # integral = num_integrate.integrate_by_trapezium(lambda t: integrand(t, m, N, r), 0, a)

    return k * integral
