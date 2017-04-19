import numpy as np
import scipy.stats as stats
import scipy.special as special
import scipy.misc as misc
import scipy.integrate as integrate
import matplotlib.pyplot as plt
import modif_bessel as iv

from decimal import *

import num_integrate
import csv


def integrand(t, m, N, r):
    # return np.float128((t ** (m - N)) * np.exp(-(t ** 2)) * special.iv(int(N), float(2 * r * t)))
    return np.float128((t ** (m - N)) * np.exp(-(t ** 2)) * iv.func(N, 2 * r * t))


def integrand_norm(m, n, p, a, t):
    return (t ** (-n)) * np.exp(-(p ** 2) * (t ** 2)) * special.i0(2 * a * t)


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


def plot_integrand_one_impulse_norm():
    x = list()
    y = list()

    for i in np.arange(0.1, 100, 0.1):
        x.append(i)
        y.append(integrand_norm(i, 1, 0, i / np.sqrt(2)))

    plt.plot(x, y)
    plt.grid()
    plt.title('график подинтеграла функции Торонто (по по инф. техн.)')
    plt.show()


def func(a, m, N, r):

    k = np.float128(2 * (r ** (N - m + 1)) * np.exp(-(r ** 2)))
    integral = np.float128(integrate.quad(lambda t: integrand(t, m, N, r), 0, a)[0])

    return np.float128(k * integral)


def func_norm(m, n, p, a):
    if n != 0:
        raise ValueError("now N must be equal 0")

    # integral = integrate.quad(lambda t: integrand_norm(m, n, p, a, t), 0, np.inf)
    integral = num_integrate.integrate_by_trapezium(lambda t: integrand_norm(m, n, p, a, t), 0, 100)
    return integral


def func_norm_2(m, n, r):
    k1 = r ** (2 * n - m + 1)
    k2 = np.exp(-(r ** 2))
    k3 = special.gamma((m + 1) / 2) / misc.factorial(n, True)
    k4 = special.hyp1f1((m + 1) / 2, n + 1, r ** 2)
    ret = k2 * k4
    print("k1 = {k1}, k2 = {k2}, k3 = {k3}, k4 = {k4}, ret = {ret}".format(k1=k1, k2=k2, k3=k3, k4=k4, ret=ret))
    return ret


def plot_func_norm_2():
    x = list()
    y = list()

    for i in np.arange(1, 30, 0.1):
        x.append(i)
        y.append(func_norm_2(3, 1, i / np.sqrt(2)))

    plt.plot(x, y)
    plt.grid()
    plt.show()


def testing_integrand(from_a, to_b):
    if to_b <= from_a:
        raise ValueError("to_b must be bigger then from_a; now to_b <= from_a")

    x = list()
    y = list()

    csvfile = open('integrand_float128.csv', 'w')
    spamwriter = csv.writer(csvfile, delimiter=' ')
    spamwriter.writerow(['x', 'y'])
    csvfile.close()

    for i in np.arange(from_a, to_b, (to_b - from_a) / 100, dtype=np.float64):
        csvfile = open('integrand_float128.csv', 'a')
        spamwriter = csv.writer(csvfile, delimiter=' ')

        m = np.float128(1.0)

        integ = integrand(i, m, np.float128(0.0), np.float128(i / np.sqrt(2)))

        print(i, integ)
        spamwriter.writerow([i, integ])
        csvfile.close()
        y.append(integ)
