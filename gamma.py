import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt


def func(z):
    return np.float128(integrate.quad(lambda t: (t ** (z - 1)) * np.exp(-t), 0, np.inf)[0])


def plot():

    x = list()
    y = list()
    for i in np.arange(-5.0, 5.0, 0.01, dtype=np.float128):
        x.append(i)
        y.append(func(i))

    plt.plot(x, y)
    plt.axis([-5, 5, -20, 20])
    plt.grid()
    plt.show()