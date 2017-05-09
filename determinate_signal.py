import scipy.integrate as integrate
import scipy.stats as stats
import scipy.special as special
import numpy as np
import matplotlib.pyplot as plt


def quantile(p, m, sigma):
    return m + sigma * np.sqrt(2) * special.erfinv(2 * p - 1)


def my_erf(x):
    return integrate.quad(lambda t: np.exp(-(t ** 2) / 2), -np.inf, x)[0] / np.sqrt(2 * np.pi)


def prob_det_2(sqrt_E2_N0, threshold_l0):
    return 1 - my_erf((threshold_l0 - 0.5 * (sqrt_E2_N0 ** 2)) / sqrt_E2_N0)


def get_prob_det(false_alarm):
    x = list()
    y = list()
    for i in np.arange(1, 16, 0.1):
        z_0 = stats.norm.ppf((1 - false_alarm), 0, i)
        ln_l0 = z_0 - (i ** 2) / 2
        x.append(i)
        y.append(prob_det_2(i, ln_l0))

    return x, y


def get_family():
    x1, y1 = get_prob_det(10 ** -4)
    x2, y2 = get_prob_det(10 ** -6)
    x3, y3 = get_prob_det(10 ** -8)
    x4, y4 = get_prob_det(10 ** -10)
    x5, y5 = get_prob_det(10 ** -12)

    return x1, y1, x2, y2, x3, y3, x4, y4, x5, y5


def plot_family():
    x1, y1, x2, y2, x3, y3, x4, y4, x5, y5 = get_family()
    plt.plot(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5)

    plt.axis([1, 16, 0, 1])
    plt.xlabel(r'$\sqrt{\frac{2E}{N_0}}$', fontsize=16, ha='left')
    plt.ylabel('D', fontsize=16)
    plt.grid()
    plt.show()
