import scipy.integrate as integrate
import scipy.stats as stats
import scipy.special as special
import numpy as np
import matplotlib.pyplot as plt


def integrate_by_trapezium(function, from_a, to_b):
    # print("from", from_a, "to", to_b)
    if to_b <= from_a:
        raise ValueError("lower param of integrate must be bigger then upper param")

    integral = np.float128(0.0)

    step = (to_b - from_a) / 10000
    x_left = from_a
    y_left = function(from_a)

    for i in np.arange(from_a + step, to_b, step):
        x_right = i
        y_right = function(i)

        integral += (y_right + y_left) * (x_right - x_left) / 2

        x_left = x_right
        y_left = y_right

    return np.float128(integral)

