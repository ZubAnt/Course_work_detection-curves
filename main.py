import determinate_signal as ds
import random_initial_phase_signal as rips
import random_inital_phase_and_amp as ripa
import matplotlib.pyplot as plt
import numpy as np
import datetime
import numpy.core.numerictypes as npt
import scipy.stats as stats

import num_integrate
import scipy.special as spec
import scipy.misc as misc
import Incoherent_inital_phase_signal as incor

import toronto
import no_toronto
import gamma
import modif_bessel

import csv
import factorial
import plot_from_log
import loss
import base64


def plot_coherent_all():

    ds_x1, ds_y1, ds_x2, ds_y2, ds_x3, ds_y3, ds_x4, ds_y4, ds_x5, ds_y5 = ds.get_family()
    rips_x1, rips_y1, rips_x2, rips_y2, rips_x3, rips_y3, rips_x4, rips_y4, rips_x5, rips_y5 = rips.get_family()
    ripa_x1, ripa_y1, ripa_x2, ripa_y2, ripa_x3, ripa_y3, ripa_x4, ripa_y4, ripa_x5, ripa_y5 = ripa.get_family()

    plt.plot(ds_x1, ds_y1, 'r', ds_x2, ds_y2, 'r', ds_x3, ds_y3, 'r', ds_x4, ds_y4, 'r', ds_x5, ds_y5, 'r',
             rips_x1, rips_y1, 'b--', rips_x2, rips_y2, 'b--', rips_x3, rips_y3, 'b--', rips_x4, rips_y4, 'b--',
             rips_x5, rips_y5, 'b--',
             ripa_x1, ripa_y1, 'g-.', ripa_x2, ripa_y2, 'g-.', ripa_x3, ripa_y3, 'g-.', ripa_x4, ripa_y4, 'g-.',
             ripa_x5, ripa_y5, 'g-.'
             )

    plt.axis([1, 16, 0, 1])
    plt.xlabel(r'$\sqrt{\frac{2E}{N_0}}$', fontsize=16, ha='left')
    plt.ylabel('D', fontsize=16)
    plt.grid()
    plt.show()


def plot_bessel():
    x = list()
    y = list()
    for i in np.arange(0, 4, 0.1):
        x.append(i)
        # y.append(spec.i1(i))
        y.append(spec.iv(0, i))

    plt.plot(x, y)
    plt.axis([0, 4, 0, 3.5])
    plt.grid()
    plt.show()


def plot_incoh_and_coh(false_alarm):
    x1, y1 = incor.get_prob_det_with_toronto_one_impulse(false_alarm, 10, 40)
    x2, y2 = rips.get_prob_det(false_alarm)
    plt.plot(x1, y1, x2, y2)
    plt.grid()
    plt.axis([0, 40, 0, 1])
    plt.title('график когерентной и не когерентной кривой для одинаковых F')
    plt.show()

def test():
    raise BaseException("test")

if __name__ == "__main__":

    # loss.log()
    # ripa.plot_family()
    # modif_bessel.test()
    # plot_coherent_all()
    incor.log_one_prob_det(3, 0.1, 20)




