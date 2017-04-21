import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt
import csv
import os
import datetime
import toronto


def mod(val):
    if val >= np.float128(0.0):
        return val
    return -val


def get_prob_det(false_alarm, from_a, to_b, N, number_step, sqrt2E_N0 = None):
    if to_b <= from_a:
        raise ValueError("to_b must be bigger then from_a; now to_b <= from_a")

    x = list()
    y = list()

    csv_file_name = "csv/D_F{F}___N{N}__EN0{EN0}.csv".format(F=false_alarm, N=N, EN0=sqrt2E_N0)
    log_data_name = "log_data/D_F{F}___N{N}__EN0{EN0}.txt".format(F=false_alarm, N=N, EN0=sqrt2E_N0)
    header_name = 'F = {F}; Nimp = {Nimp}; Range: [{a}, {b}] EN0 = {EN0}'.format(F=false_alarm,
                                                                                 Nimp=N, EN0=sqrt2E_N0,
                                                                                 a=from_a, b=to_b)

    csv_file = open(csv_file_name, 'w')
    data_file = open(log_data_name, 'w')
    csv_writer = csv.writer(csv_file, delimiter=' ')

    csv_writer.writerow([header_name])
    data_file.write(header_name + "\n")
    csv_writer.writerow(['x', 'y'])

    df = 2 * N  # число степеней свободы - для одного имплься = 2

    for i in np.arange(from_a, to_b, (to_b - from_a) / number_step, dtype=np.float64):

        C = stats.chi2.ppf(1 - false_alarm, df, 0, i)
        a = np.float128(np.sqrt(C / 2))
        m = np.float128(2 * N - 1)
        p = np.float128(N - 1)
        if sqrt2E_N0 is None:
            r = np.float128(np.sqrt(N) * i / np.sqrt(2))
        else:
            r = np.float128(np.sqrt(N) * sqrt2E_N0 / np.sqrt(2))

        D = np.float128(1 - toronto.func(a, m, p, r))

        data_str = "i = {i}, C = {C}, a = {a}, m = {m}, p = {p}, r = {r}, D = {D}". \
            format(i=i, C=C, a=a, m=m, p=p, r=r, D=D)

        if D == np.inf:
            error = "D == np.inf; {data}".format(data=data_str)
            raise RuntimeError(error)

        if D == np.nan:
            error = "D == np.nan; {data}".format(data=data_str)
            raise RuntimeError(error)

        if mod(D) > np.float128(10 ** (-3)):
            x.append(i)
            y.append(D)
            print(i, D)
            data_file.write(data_str + "\n")
            csv_writer.writerow([i, D])

        if np.float128(1.0) - D < np.float128(10 ** (-2)):
            break

    data_file.close()
    csv_file.close()
    return x, y


def init():
    dirs = ['csv', 'log', 'log_data']
    for dir_name in dirs:
        try:
            os.mkdir(dir_name)
        except FileExistsError:
            pass


def plot(F, from_a, to_b, N):

    from_a = np.float128(from_a)
    to_b = np.float128(to_b)
    init()

    x, y = get_prob_det(F, from_a, to_b, N, 100)

    plt.plot(x, y)
    plt.axis([0, 40, 0, 1])
    plt.grid()
    plt.title("график кривой обнаружения с функций торонто по инф. техн.")
    plt.show()


def plot_family():

    x1, y1 = get_prob_det(10 ** -4)
    x2, y2 = get_prob_det(10 ** -6)
    x3, y3 = get_prob_det(10 ** -8)

    plt.plot(x1, y1, x2, y2, x3, y3)
    plt.grid()
    plt.show()


def log_prob_det():

    false_alam = 10 ** -7
    from_a = np.float128(0.1)
    to_b = np.float128(40.0)
    init()
    max_n = 100
    for N in range(1, max_n + 1):

        try:
            get_prob_det(false_alam, from_a, to_b, N, 100)

        except RuntimeError as err:

            err_file_name = "log/err_log.log"
            curr_time = datetime.datetime.now()
            file = open(err_file_name, 'a')
            file.write("{time} ERROR: {error}\n".format(time=curr_time, error=err))
            file.close()

        except:

            err_file_name = "log/err_log.log"
            curr_time = datetime.datetime.now()
            file = open(err_file_name, 'a')
            file.write("{time} FATAL ERROR: N = {N}\n".format(time=curr_time, N=N))
            file.close()



