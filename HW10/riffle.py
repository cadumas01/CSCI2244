# Top to Random Shuffle
import random
import math


def top_to_random(in_l):
    l = list(in_l)

    top = l[0]
    l.pop(0)

    rand_ind = random.randint(0, len(l))

    l.insert(rand_ind, top)
    return l


def gsr(in_l):
    l = list(in_l)
    shuffled = [0]*len(l)

    cut_ind = cut_index(l)

    left_deck = l[0:cut_ind]
    right_deck = l[cut_ind:]

    for i in range(0, len(shuffled)):
        if random.random() < (len(left_deck) / (len(left_deck) + len(right_deck))): # left card falls
            shuffled[i] = left_deck[0]
            left_deck.pop(0)
        else: # right card falls
            shuffled[i] = right_deck[0]
            right_deck.pop(0)

        #print("left deck", left_deck)
       # print("right deck", right_deck)
    return shuffled


# Generates a deck cut index based on list l
def cut_index(l):
    sum = 0
    for i in range(0, len(l)):
        sum += random.randint(0, 1)

    return sum


# returns 1 if i appears before j in l
def test_order(i, j, l):
    for e in range(0, len(l)):
        if i == l[e]:
            return 1
        elif j == l[e]:
            return 0
    return 0


# prob is the probability that i is above j
def num_trials(err, prob):
    p = .5
    return (p * (1-p)) / (prob * (err ** 2))


# n is number of cards in l; l lis i 0 to n; k is number of shuffles; i and j are values within 0 to n
def gsr_order_prob(n, k, i, j, err, prob):
    return monte_carlo(n, k, i, j, err, prob, gsr)


# n is number of cards in l; l lis i 0 to n; k is number of shuffles; i and j are values within 0 to n
def top_to_random_order_prob(n, k, i, j, err, prob):
    return monte_carlo(n, k, i, j, err, prob, top_to_random)


def monte_carlo(n, k, i, j, err, prob, shuffle_func):
    n_trials = math.ceil(num_trials(err, prob))
    l = list(range(0, n))

    sum = 0
    for t in range(n_trials):
        sum += trial(l, k, i, j, shuffle_func)

    return sum / n_trials


def trial(l, k_shuffles, i, j, shuffle_func):
    for k in range(k_shuffles):
        l = shuffle_func(l)

    return test_order(i, j, l)


def main():
    n = 10
    k = 8
    i = 2
    j = 3
    err = .05
    prob = .05
    print(gsr_order_prob(n, k, i, j, err, prob))
    print(top_to_random_order_prob(n, k, i, j, err, prob))


if __name__ == "__main__":
    main()

