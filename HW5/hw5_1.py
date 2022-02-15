import numpy as np
import random


# Monty Hall Problem

def main():
    N = 100000

    # winners = choices = {0,1,2}
    winners = np.random.randint(0,3, size=(1,N))
    choices = np.random.randint(0,3, size=(1,N))

    v_reveal = np.vectorize(reveal)
    v_final_choice = np.vectorize(final_choice)

    print("Winners:\n", winners)
    print("Choices:\n", choices)
    reveals = v_reveal(winners, choices)

    final_choices = v_final_choice(choices,reveals)

    # True = not 0
    stays = np.equal(final_choices, choices)


    wins_stays = np.logical_and((stays != 0), (final_choices - winners == 0))
    win_switches = np.logical_and((stays == 0), (final_choices - winners == 0))

    n_wins_stays = np.count_nonzero(wins_stays)
    n_stays = np.count_nonzero(stays)

    n_wins_switches= np.count_nonzero(win_switches)
    n_switches = N - n_stays

    print("Stays", n_wins_stays, "/", n_stays, " = ", n_wins_stays/n_stays)
    print("Switches", n_wins_switches, "/", n_switches, " = ", n_wins_switches/n_switches)



def reveal(winner, choice):
    if choice == winner:
        return randint_exclude(0, 2, winner)
    elif abs(choice - winner) == 1:
        return (max(choice, winner) + 1) % 3
    else: # abs(choice - winner) == 2
        return 1


def final_choice(choice, reveal):
    if random.randint(0,1) == 1:
        return choice
    elif abs(choice - reveal) == 1:
        return (max(choice, reveal) + 1) % 3
    else:  # abs(choice - reveal) == 2
        return 1





def randint_exclude(a,b, exclude):
    x = random.randint(a,b)
    while x == exclude:
        x = random.randint(a,b)

    return x

main()