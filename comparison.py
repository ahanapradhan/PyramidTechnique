import matplotlib.pyplot as plt
import numpy as np
import math

page_size = 4096
n = 100000


def balanced_function(d, q):
    ceff = page_size / ((d + 1) * 1)  # assuming each key and dimension takes 1 byte each
    total_pages = n / ceff
    d_dash = math.log(total_pages, 2)
    result = total_pages * min(1, (0.5 / (1 - q)) ** d_dash)
    result = result / total_pages
    return result


def pyramid_function(d, q):
    ceff = page_size / ((d + 1) * 1)  # assuming each key and dimension takes 1 byte each
    total_pages = n / ceff
    result = (2 * d + n * (1 - (2 * q - 1) ** (d + 1))) / (2 * ceff * (d + 1) * (1 - q))
    result = result / total_pages
    return result


q_values = [0.2, 0.4, 0.6, 0.8]
for q_val in q_values:
    xpoints = np.array([5, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 30, 40, 50, 60, 70, 80, 90, 100])  # values of d
    ypoints = np.array([balanced_function(i, q_val) for i in xpoints])
    pyramidpoints = np.array([pyramid_function(i, q_val) for i in xpoints])

    plt.plot(xpoints, ypoints, label="balanced split")
    plt.plot(xpoints, pyramidpoints, label="pyramid")
    plt.legend(loc="upper right")
    plt.show()

