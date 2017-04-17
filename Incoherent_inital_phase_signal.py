import scipy.integrate as integrate
import scipy.stats as stats
import scipy.special as special
import numpy as np
import matplotlib.pyplot as plt
import num_integrate

import toronto
import no_toronto

import csv


def get_prob_det_with_toronto_one_impulse(false_alarm, from_a, to_b):
    if to_b <= from_a:
        raise ValueError("to_b must be bigger then from_a; now to_b <= from_a")

    x = list()
    y = list()

    csvfile = open('tor_in_work.csv', 'w')
    spamwriter = csv.writer(csvfile, delimiter=' ')
    spamwriter.writerow(['x', 'y'])
    csvfile.close()

    df = 2  # число степеней свободы - для одного имплься = 2
    for i in np.arange(from_a, to_b, (to_b - from_a) / 10):

        c = stats.chi2.ppf(1 - false_alarm, df, 0, i)

        x.append(i)
        d = 1 - toronto.func(np.sqrt(c / 2), 1, 0, i / np.sqrt(2))
        y.append(d)

        csvfile = open('tor_in_work.csv', 'a')
        spamwriter = csv.writer(csvfile, delimiter=' ')
        spamwriter.writerow([i, d])
        print(i, d)
        csvfile.close()

    return x, y


def get_prob_det_without_toronto_one_impulse(false_alarm):

    x = list()
    y = list()

    df = 2  # число степеней свободы - для одного имплься = 2
    for i in np.arange(0.1, 40, 0.1):
        x.append(i)

        c = stats.chi2.ppf(1 - false_alarm, df, 0, i)

        # k = 0.5
        # sqrt_E2_N0 = i
        # integral = num_integrate.integrate_by_trapezium(
        #     lambda z: np.exp(- ((sqrt_E2_N0 ** 2 + z) / 2)) * special.i0(np.sqrt((sqrt_E2_N0 ** 2) * z)), c, 10000)
        # y.append(k * integral)

        integral = integrate.quad(lambda s: no_toronto.integrand_shirman(s, 1, i ** 2), c, np.inf)[0]
        y.append(integral)

    return x, y


def plot_for_one_imp_with_toronto():
    # x1, y1 = get_prob_det_with_toronto_one_impulse(10 ** -4, 10, 30)
    # x2, y2 = get_prob_det_with_toronto_one_impulse(10 ** -6, 10, 40)
    # x3, y3 = get_prob_det_with_toronto_one_impulse(10 ** -8, 10, 50)

    x2, y2 = get_prob_det_with_toronto_one_impulse(10 ** -6, 10, 25)
    plt.plot(x2, y2)

    # plt.plot(x1, y1, x2, y2, x3, y3)
    plt.axis([0, 60, 0, 1])
    plt.grid()
    plt.title("график кривой обнаружения с функций торонто по инф. техн.")
    plt.show()


def plot_for_one_imp_without_toronto():

    x1, y1 = get_prob_det_without_toronto_one_impulse(10 ** -4)
    x2, y2 = get_prob_det_without_toronto_one_impulse(10 ** -6)
    x3, y3 = get_prob_det_without_toronto_one_impulse(10 ** -8)

    plt.plot(x1, y1, x2, y2, x3, y3)
    plt.grid()
    plt.title("график кривой обнаружения без функции торонто")
    plt.show()

