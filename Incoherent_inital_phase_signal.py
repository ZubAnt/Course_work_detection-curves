import scipy.integrate as integrate
import scipy.stats as stats
import scipy.special as special
import numpy as np
import matplotlib.pyplot as plt
import num_integrate
import csv

import toronto
import no_toronto


def get_prob_det_with_toronto_one_impulse(false_alarm, from_a, to_b, N):
    if to_b <= from_a:
        raise ValueError("to_b must be bigger then from_a; now to_b <= from_a")

    x = list()
    y = list()
    log_file_name = "D_F{F}___N{N}.csv".format(F=false_alarm, N=N)

    csvfile = open(log_file_name, 'w')
    spamwriter = csv.writer(csvfile, delimiter=' ')
    header = 'F = {F}; Nimp = {Nimp}; Range: [{a}, {b}]'.format(F=false_alarm, Nimp=N, a=from_a, b=to_b)
    spamwriter.writerow([header])
    print(header)
    spamwriter.writerow(['x', 'y'])
    csvfile.close()

    df = 2 * N  # число степеней свободы - для одного имплься = 2
    for i in np.arange(from_a, to_b, (to_b - from_a) / 50, dtype=np.float64):
        x.append(i)
        csvfile = open(log_file_name, 'a')
        spamwriter = csv.writer(csvfile, delimiter=' ')

        C = stats.chi2.ppf(1 - false_alarm, df, 0, i)
        a = np.float128(np.sqrt(C / 2))
        m = np.float128(2 * N - 1)
        p = np.float128(N - 1)
        r = np.float128(np.sqrt(N) * i / np.sqrt(2))
        D = np.float128(1 - toronto.func(a, m, p, r))
        print(i, D)
        spamwriter.writerow([i, D])
        csvfile.close()
        y.append(D)

        if (np.float128(1) - D) < np.float128(10 ** (-3)):
            print("1 - D < 0.001")
            break

    return x, y


def get_prob_det_with_toronto_one_impulse_norm(false_alarm, from_a, to_b):
    if to_b <= from_a:
        raise ValueError("to_b must be bigger then from_a; now to_b <= from_a")

    x = list()
    y = list()

    df = 2  # число степеней свободы - для одного имплься = 2
    for i in np.arange(from_a, to_b, (to_b - from_a) / 50):

        c = stats.chi2.ppf(1 - false_alarm, df, 0, i)

        x.append(i)
        # np.sqrt(c / 2)
        d = toronto.func_norm(1, 0, i / np.sqrt(2), 1)
        y.append(d)
        print(i, d)

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
    # x1, y1 = get_prob_det_with_toronto_one_impulse(10 ** -4, 1, 30)
    # x2, y2 = get_prob_det_with_toronto_one_impulse(10 ** -6, 1, 30)
    # x3, y3 = get_prob_det_with_toronto_one_impulse(10 ** -8, 1, 30)

    false_alam = 10 ** -6
    from_a = np.float128(1.0)
    to_b = np.float128(40.0)

    x1, y1 = get_prob_det_with_toronto_one_impulse(false_alam, from_a, to_b, 1)
    x2, y2 = get_prob_det_with_toronto_one_impulse(false_alam, from_a, to_b, 2)
    x3, y3 = get_prob_det_with_toronto_one_impulse(false_alam, from_a, to_b, 3)

    # plt.plot(x1, y1)
    # plt.plot(x2, y2)
    # plt.plot(x1, y1, x2, y2)
    plt.plot(x1, y1, x2, y2, x3, y3)
    plt.axis([0, 40, 0, 1])
    plt.grid()
    plt.title("график кривой обнаружения с функций торонто по инф. техн.")
    plt.show()


def plot_for_one_imp_with_toronto_norm():
    x1, y1 = get_prob_det_with_toronto_one_impulse_norm(10 ** -4, 0, 30)
    x2, y2 = get_prob_det_with_toronto_one_impulse_norm(10 ** -6, 0, 40)
    x3, y3 = get_prob_det_with_toronto_one_impulse_norm(10 ** -8, 0, 50)

    plt.plot(x1, y1, x2, y2, x3, y3)
    plt.axis([0, 60, 0, 1])
    plt.grid()
    plt.title("график кривой обнаружения с обычной функций торонто")
    plt.show()


def plot_for_one_imp_without_toronto():

    x1, y1 = get_prob_det_without_toronto_one_impulse(10 ** -4)
    x2, y2 = get_prob_det_without_toronto_one_impulse(10 ** -6)
    x3, y3 = get_prob_det_without_toronto_one_impulse(10 ** -8)

    plt.plot(x1, y1, x2, y2, x3, y3)
    plt.grid()
    plt.title("график кривой обнаружения без функции торонто")
    plt.show()

