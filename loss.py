import random_initial_phase_signal as rips
import Incoherent_inital_phase_signal as incor
import os
import datetime
import numpy as np
import toronto
import scipy.stats as stats

file_name_loss = "log/loss.log"


def init():
    dirs = ['csv', 'log', 'log_data']
    for dir_name in dirs:
        try:
            os.mkdir(dir_name)
        except FileExistsError:
            pass


# Возвращает отношение сигнал шум для одного импульса в пачке из N импульсов
def get_EN0(sqrt2E_N0, N):
    return (sqrt2E_N0 ** 2) / (2 * N)


def get_EN0_incor(sqrt2E_N0_incor, N):
    return (sqrt2E_N0_incor ** 2) / (2 * N)

def log():

    init()
    file_loss = open(file_name_loss, 'w')
    F = 10 ** (-7)
    D = 0.9
    # sqrt2E_N0 = rips.get_sqrt2E_N0(F, D)
    sqrt2E_N0 = 6.85
    Ep0 = (sqrt2E_N0 ** 2) / 2
    # print("sqrt2E_N0 = ", sqrt2E_N0)
    from_a = 1
    to_b = 10
    N = [25]
    try:
        for n in N:
            x, y = incor.get_prob_det(F, from_a, to_b, n, 100)
            sqrt2E_N0_incor = rips.get_sqrt2E_N0_from_curve(x, y, D)
            Epk = Ep0 / n
            EN0_incor = (sqrt2E_N0_incor ** 2) / 2
            ans = Ep0 / EN0_incor
            print('sqrt2E_N0_incor = ', sqrt2E_N0_incor, '; Ep0 = ', Ep0, '; Epk = ', Epk,
                  '; EN0_incor = ', EN0_incor)
            print(ans, 10 * np.log10(ans))

    except RuntimeError as err:

        err_file_name = "log/err_log.log"
        curr_time = datetime.datetime.now()
        file = open(err_file_name, 'a')
        file.write("{time} ERROR: {error}\n".format(time=curr_time, error=err))
        file.close()

    # except:
    #
    #     err_file_name = "log/err_log.log"
    #     curr_time = datetime.datetime.now()
    #     file = open(err_file_name, 'a')
    #     file.write("{time} FATAL ERROR\n".format(time=curr_time))
    #     file.close()

    file_loss.close()
