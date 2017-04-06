import numpy as np
import scipy.stats as stats
import scipy.special as special
import scipy.integrate as integrate
import matplotlib.pyplot as plt


def bessel(N, x):
    if N == 0:
        return special.j0(x)
    elif N == 1:
        return special.j1(x)
    else:
        raise ValueError("N != 0 and N != 1")


def integrand_inform_techn(z, N, q_in_square):
    return (
        (z / (N * q_in_square)) ** ((N - 1) / (2 ** (N - 1))) *
        np.exp(- (N * q_in_square + z) / 2) *
        bessel(N - 1, np.sqrt(N * q_in_square * z))
         )


def integrand_shirman(s, M, q_in_square):
    k_disc_M = M * q_in_square / 2
    return (
        (s / k_disc_M) ** ((M - 1) / 2) *
        np.exp(- (s + k_disc_M)) *
        bessel(M - 1, 2 * s * k_disc_M)
         )


def plot_integrand_one_impulse():
    x = list()
    y1 = list()
    y2 = list()

    sqrt_2E_N0 = np.arange(0.1, 40, 0.1)

    for i in sqrt_2E_N0:
        x.append(i)
        y1.append(integrand_inform_techn(i, 1, i ** 2))
        y2.append(integrand_shirman(i, 1, i ** 2))

    plt.plot(x, y1, x, y2)
    plt.grid()
    plt.axis([0, 10, -0.1, 1])
    plt.title("График подинтеграла кривой обнаружения для некогерентного случая по Ширману и по инф. техн.")
    plt.show()

