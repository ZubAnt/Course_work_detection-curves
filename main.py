import determinate_signal as ds
import random_initial_phase_signal as rips
import random_inital_phase_and_amp as ripa
import matplotlib.pyplot as plt
import numpy as np
import datetime
import numpy.core.numerictypes as npt
import scipy.stats as stats

import chi2_mod
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

    # Plot integrand
    # toronto.plot_integrand_one_impulse()      # график подинтеграла для некогерентного случая по по инф. техн. с Торонто
    # no_toronto.plot_integrand_one_impulse()   # график подинтеграла для некогерентного случая по Ширману и по инф. техн.

    # incor.plot_for_one_imp_with_toronto()     # график интеграла с функций торонто
    # print(stats.chi2.ppf(1 - 10**(-4), 2))
    # incor.plot_for_one_imp_without_toronto()  # график интеграла без функции торонто
    # incor.plot_for_one_imp_with_toronto_norm()

    # toronto.plot_func_norm_2()
    # plot_incoh_and_coh(10 ** -4)              # график когерентной и не когерентной кривой для одинаковых F
    # plot_bessel()

    # false_alam = np.float128(1.0)
    # print(false_alam)
    # print(np.sin(np.float128(3.14 / 2)))
    # gamma.plot()
    # modif_bessel.plot()
    # print(spec.gamma(np.float128(3.14 / 2)))

    # toronto.testing_integrand(0, 50)
    # factorial.test()
    # modif_bessel.test()
    # plot_from_log.plot()
    incor.log_prob_det()




