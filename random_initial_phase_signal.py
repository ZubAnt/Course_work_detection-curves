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

    return k * my_summ(lambda k: maclor(coeff_discount, k) * my_summ(lambda l: maclor(ln_inv_f, l), 0, k), 0, 150)


def get_prob_det(false_alarm):
    x = list()
    y = list()
    for i in np.arange(1, 12, 0.1):
        x.append(i)
        y.append(marqumq(i, false_alarm))

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
    plt.grid()
    plt.show()






