import numpy as np
from scipy.stats import norm
import math

def q1():
    Q = np.array([[.5, .333], [.5, .25]])
    R = np.array([[.167, 0], [0, .25]])

    I2 = np.identity(2)

    S = np.linalg.inv(np.subtract(I2, Q))
    SR = np.dot(S, R)

    print("\n#1", SR)
    # sum and display 0th row
    # print(np.sum(S, 1)[0])


def q2():
    Q = np.array([[.5, .5, 0, 0], [12/25, .5, 1/50, 0], [12/25, .5, 0, 1/50], [.5, 0, 0, 0]])
    R = np.array([[0],[0],[0],[.5]])

    I = np.identity(4)

    S = np.linalg.inv(np.subtract(I, Q))

    # sum and display 0th row
    print("\n#2", np.sum(S, 1)[0])


def q3():
    p = .7
    Q = np.array([[1 - p, p, 0], [0, p, 1-p], [1-p, 0, 0]])

    I = np.identity(3)

    S = np.linalg.inv(np.subtract(I, Q))

    print("\n#3", np.sum(S, 1)[0])


def q4():
    n = 217
    exp_x = 8
    var_x = 8

    exp_s = n * exp_x
    var_s = n * var_x

    print("\n#4", norm.ppf(.9, exp_s, math.sqrt(var_s)))


q1()
q2()
q3()
q4()