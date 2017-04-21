import random_initial_phase_signal as rips
import Incoherent_inital_phase_signal as incor
import os
import datetime


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
    file_loss = open(file_name_loss, 'a')
    F = 10 ** (-7)
    D = 0.9
    sqrt2E_N0 = rips.get_sqrt2E_N0(F, D)

    try:
        x2, y2 = incor.get_prob_det(F, 0.1, 40, 2, 200, sqrt2E_N0)
        sqrt2E_N0_incor2 = rips.get_sqrt2E_N0_from_curve(x2, y2, D)
        file_loss.write(sqrt2E_N0_incor2)
        file_loss.write("\n")

        x5,y5 = incor.get_prob_det(F, 0.1, 30, 5, 200, sqrt2E_N0)
        sqrt2E_N0_incor5 = rips.get_sqrt2E_N0_from_curve(x5, y5, D)
        file_loss.write(sqrt2E_N0_incor5)
        file_loss.write("\n")

        x10, y10 = incor.get_prob_det(F, 0.1, 30, 10, 200, sqrt2E_N0)
        sqrt2E_N0_incor10 = rips.get_sqrt2E_N0_from_curve(x10, y10, D)
        file_loss.write(sqrt2E_N0_incor10)
        file_loss.write("\n")

        x100, y100 = incor.get_prob_det(F, 10 ** (-4), 20, 100, 200, sqrt2E_N0)
        sqrt2E_N0_incor100 = rips.get_sqrt2E_N0_from_curve(x100, y100, D)
        file_loss.write(sqrt2E_N0_incor100)
        file_loss.write("\n")

        x1000, y1000 = incor.get_prob_det(F, 10 ** (-8), 10, 10000, 200, sqrt2E_N0)
        sqrt2E_N0_incor1000 = rips.get_sqrt2E_N0_from_curve(x1000, y1000, D)
        file_loss.write(sqrt2E_N0_incor1000)
        file_loss.write("\n")


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


    file.close()