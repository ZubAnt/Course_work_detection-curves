import csv
import matplotlib.pyplot as plt


def get_coord(file_name):
    file = open(file_name, 'r')
    header = file.readline()
    file.readline()

    x = list()
    y = list()

    for line in file:
        coord = line.rstrip().split()
        if len(coord) != 2:
            raise ValueError("len(coord) != 2")
        x.append(coord[0])
        y.append(coord[1])
    file.close()

    return x, y, header


def plot():
    x1, y1, header = get_coord('D_F1e-06___N3.csv')
    plt.plot(x1, y1)
    plt.title(header)
    plt.axis([0, 40, 0, 1])
    plt.gray()
    plt.show()


