import random_initial_phase_signal as rips
import Incoherent_inital_phase_signal as incor
import os
import datetime
import numpy as np


file_name_loss = "log/loss.log"


def init():
    dirs = ['csv', 'log', 'log_data']
    for dir_name in dirs:
        try:
            os.mkdir(dir_name)
        except FileExistsError:
            pass


def log():

    init()
    file_loss = open(file_name_loss, 'w')
    F = 10 ** (-7)
    D = 0.9
    sqrt2E_N0 = rips.get_sqrt2E_N0(F, D)

    from_a = 10 ** -4
    to_b = 20
    N = [2, 5, 10]
    try:
        for n in N:
            x, y = incor.get_prob_det(F, from_a, to_b, n, 500, sqrt2E_N0)
            sqrt2E_N0_incor = rips.get_sqrt2E_N0_from_curve(x, y, D)
            file_loss.write("N = {N}; sqrt2E_N0_incor = {s}\n".format(N=n, s=str(sqrt2E_N0_incor)))

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
        file.write("{time} FATAL ERROR\n".format(time=curr_time))
        file.close()

    file_loss.close()