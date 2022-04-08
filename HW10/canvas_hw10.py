import math

def expected_val(X):
    s = 0
    for i in range(len(X)):
        s += X[i][0] * X[i][1]

    return s


def variance(X):
    expected = expected_val(X)

    # Y is the new random variable: (X - E[X])^2
    Y = []
    for i in range(len(X)):
        Y.append((((X[i][0] - expected)**2), X[i][1]))

    return expected_val(Y)


def p_i(n, i, p_box_has_toy):
    return p_box_has_toy * (n - i + 1) / n


def q4():
    sum = 0
    n = 19
    for i in range(1, n + 1):
        sum += 1 / p_i(n, i, .5)

    return sum


def q3():
    sum = 0
    n = 12
    for i in range(1, n + 1):
        sum += 1 / p_i(n, i, .9)

    return sum


def main():
    # 2
    n = 250
    X = [(-1,.9), (2,.1)]
    x_exp = expected_val(X)
    x_var = variance(X)

    s_exp = x_exp * n
    s_var = x_var * n

    standard_dists = 1.555


    print("#2", standard_dists * math.sqrt(s_var) + s_exp)

    print("#3", q3())
    print("#4", q4())


main()