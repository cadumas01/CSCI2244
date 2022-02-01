import numpy


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
    t = (2 * (6 ** d)) ** 2
    arr = sum_dice_roll(t, d)
    prob_step = 1 / (6 ** d)

    x_rel_freq = freq(x, arr)/t

    # finds the nearest relative frequency in prob_step units
    return round(x_rel_freq/prob_step) * prob_step


# Returns the frequency of x occurring in arr
def freq(x, arr):
    num_x = numpy.equal(arr, x)
    return numpy.count_nonzero(num_x)


# Creates a d by n array of random integers [1,6]
def dice_roll(t, d):
    return numpy.random.randint(1, 7, size=(t, d))


# Creates a 1 by n array of the sum of d dice rolls in each collum; (vertically sums d dice_roll arrays)
def sum_dice_roll(t, d):
    return dice_roll(t, d).sum(axis=1)

