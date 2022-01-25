import numpy as np
import math
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt


def galileo(d, a, b):
    prob_a = prob(a, d)
    prob_b = prob(b, d)

    if prob_a < prob_b:
        return -1
    elif prob_a == prob_b:
        return 0
    else:
        return 1


# Rounds the sample relative_frequency of x to its nearest 'integer' step
def prob(x, d):
    t = 6**(2*d)
    n = math.ceil(t / d)  # not sure how many rolls to do.
    arr = sum_dice_roll(n, d)
    prob_step = 1 / (6 ** d)

    x_rel_freq = freq(x, arr)/n

    # finds the nearest relative frequency in prob_step units
    return round(x_rel_freq/prob_step) * prob_step


# Returns the frequency of x occurring in arr
def freq(x, arr):
    num_x = np.equal(arr, x)
    return np.count_nonzero(num_x)


# Creates a d by n array of random integers [1,6]
def dice_roll(n, d):
    return np.random.randint(1, 7, size=(n, d))


# Creates a 1 by n array of the sum of d dice rolls in each collum; (vertically sums d dice_roll arrays)
def sum_dice_roll(n, d):
    return dice_roll(n, d).sum(axis=1)


def hist(n, d):
    arr = sum_dice_roll(n,d)
    bins = 6*d - d + 1
    plt.hist(arr, density=True, bins=bins)
    plt.ylabel("Frequency")
    plt.xlabel("Data")
    plt.show()
    print(bins)


if __name__ == "__main__":
    # hist(5000000,2)
    zeros = 0
    not_zeros = 0
    for i in range(1000):
        if (galileo(3,10,11)) == 0:
            zeros = zeros + 1
        else:
            not_zeros = not_zeros + 1

    print("Zeros =", zeros, "\n", "Not Zeros =", not_zeros)
