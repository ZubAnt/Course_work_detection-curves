from scipy.stats import chi2
import matplotlib.pyplot as plt
import numpy as np


def plot_chi2(df):
    x = list()
    y = list()
    for i in np.arange(0, 14, 0.1):
        x.append(i)
        # y.append(stats.chi2(i))
        y.append(chi2.pdf(i, df))

    plt.plot(x, y)
    plt.axis([0, 14, 0, 0.5])
    plt.grid()
    plt.show()
