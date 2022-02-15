import random
import numpy as np
from scipy.special import binom, factorial

def main():
    n = 20
    k = 18
    N = 300000

    data = np.empty(N)


    for i in range(N):
        data[i] = tournament(n)

    prob_k = count(data, k)/(N)
    print(data)
    print("The Monte Carlo simulation for n=", n, "and k=", k, "is", prob_k)
    print("The formula gives:", formula(n,k))

def formula(n,k):
    return binom((n+k-1), k) * ((.5**(n+k-1)))


def count(data, k):
    return np.count_nonzero(data == k)


def tournament(n_games):
    n1 = 0  # Player 2's wins
    n2 = 0  # Player 1's wins
    p = .5

    # end once EITHER player wins
    while n1 < n_games and n2 < n_games:
        if game(p):
            n1 += 1
        else:
            n2 += 1

    # returns the loser's number of wins
    return min(n1, n2)


def game(p):
    return random.randint(0, 1) == 1


main()