import numpy as np


def square_pi(n):
    xy = np.random.random((n, 2)) ** 2
    counts = np.sum((xy[:, 0] + xy[:, 1]) <= 1)
    print("pi aproximat la:", 4*counts/n)
    return 4*counts/n


square_pi(5000)
