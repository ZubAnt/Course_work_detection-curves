import determinate_signal as ds
import random_initial_phase_signal as rips
import random_inital_phase_and_amp as ripa
import matplotlib.pyplot as plt


def plot_all():

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


if __name__ == "__main__":

    plot_all()
    # ds.plot_determinate()
    # rips.plot_determinate()
    # ripas.plot_determinate()

