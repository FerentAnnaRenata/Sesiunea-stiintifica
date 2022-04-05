import numpy as np


def pi(n):
    x_y = np.random.random((n, 2)) ** 2
    counts = np.sum((x_y[:, 0] + x_y[:, 1]) <= 1)
    print("pi aproximat la:", 4*counts/n)
    return 4*counts/n


pi(5000)
