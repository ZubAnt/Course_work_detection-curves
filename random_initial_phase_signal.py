import numpy as np
import matplotlib.pyplot as plt


def my_summ(func, x_from, x_to):
    val = 0
    for i in range(x_from, x_to + 1):
        val += func(i)
    return val


def maclor(val, degree):
    return (val ** degree) / np.math.factorial(degree)


def marqumq(sqrt_E2_N0, false_alarm):

    coeff_discount = (sqrt_E2_N0 ** 2) / 2
    ln_inv_f = np.log(1 / false_alarm)

    k = np.exp(-coeff_discount - ln_inv_f)

    return k * my_summ(lambda k: maclor(coeff_discount, k) * my_summ(lambda l: maclor(ln_inv_f, l), 0, k), 0, 100)


def get_prob_det(false_alarm):
    x = list()
    y = list()
    for i in np.arange(1, 12, 0.01):
        x.append(i)
        y.append(marqumq(i, false_alarm))

    return x, y


def get_сurve(false_alarm):
    x1, y1 = get_prob_det(false_alarm)
    return x1, y1


def plot_curve(false_alarm):

    x, y = get_сurve(false_alarm)
    plt.plot(x, y)
    plt.axis([1, 16, 0, 1])
    plt.grid()
    plt.show()


def get_sqrt2E_N0(F, D):
    x, y = get_сurve(F)
    return get_sqrt2E_N0_from_curve(x, y, D)


def get_sqrt2E_N0_from_curve(x, y, D):
    ind = 0
    ind_min_delta = 0
    min_delta = 1
    for prob_det_it in y:
        if D - prob_det_it < min_delta and (D - prob_det_it) > 0:
            ind_min_delta = ind
            min_delta = (D - prob_det_it)
        ind += 1

    print(ind_min_delta, x[ind_min_delta], y[ind_min_delta], min_delta)

    return x[ind_min_delta]






