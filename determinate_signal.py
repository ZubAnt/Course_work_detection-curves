import scipy.integrate as integrate
import scipy.stats as stats
import scipy.special as special
import numpy as np
import matplotlib.pyplot as plt
import num_integrate


def quantile(p, m, sigma):
    return m + sigma * np.sqrt(2) * special.erfinv(2 * p - 1)


def my_erf(x):
    return integrate.quad(lambda t: np.exp(-(t ** 2) / 2), -np.inf, x)[0] / np.sqrt(2 * np.pi)
    # return num_integrate.integrate_by_trapezium(lambda t: np.exp(-(t ** 2) / 2), -100, x) / np.sqrt(2 * np.pi)


def prob_det_1(sqrt_E2_N0, threshold_z0):

    k = 1 / np.sqrt(2 * np.pi) * sqrt_E2_N0
    E2_N0 = sqrt_E2_N0 ** 2

    # return integrate.quad(lambda z: k * np.exp(- ((z - E2_N0) ** 2) / (2 * E2_N0)), threshold_z0, np.inf)[0]
    return num_integrate.integrate_by_trapezium(lambda z: k * np.exp(- ((z - E2_N0) ** 2) / (2 * E2_N0)), threshold_z0, 200)


def prob_det_2(sqrt_E2_N0, threshold_l0):
    return 1 - my_erf((threshold_l0 - 0.5 * (sqrt_E2_N0 ** 2)) / sqrt_E2_N0)


def get_prob_det(false_alarm):
    x = list()
    y = list()
    for i in np.arange(1, 16, 0.1):
        # z_0 = quantile((1 - false_alarm), 0, i)
        z_0 = stats.norm.ppf((1 - false_alarm), 0, i)
        ln_l0 = z_0 - (i ** 2) / 2

        x.append(i)
        y.append(prob_det_2(i, ln_l0))
        print(i)
        # y.append(prob_det_1(i, z_0))
    return x, y


def get_family():
    x1, y1 = get_prob_det(10 ** -4)
    x2, y2 = get_prob_det(10 ** -6)
    x3, y3 = get_prob_det(10 ** -8)
    x4, y4 = get_prob_det(10 ** -10)
    x5, y5 = get_prob_det(10 ** -12)

    return x1, y1
    # return x1, y1, x2, y2, x3, y3, x4, y4, x5, y5


def plot_family():
    x1, y1, x2, y2, x3, y3, x4, y4, x5, y5 = get_family()
    plt.plot(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5)
    # x1, y1 = get_family()
    # plt.plot(x1, y1)

    plt.axis([1, 16, 0, 1])
    plt.grid()
    plt.show()
