# Canvas Quiz 8

def q1():

    rand_var = []
    size = 4

    p4 = .3
    p1_3 = (1-p4)/(size-1)

    for x in range(1, size + 1):
        if x == 4:
            rand_var.append((x ** 3,p4))
        else:
            rand_var.append((x ** 3,p1_3))

    print("#1:", variance(rand_var))


def q2():
    rand_var = []
    size = 4

    p4 = .33
    p1_3 = (1-p4)/(size-1)

    for x in range(1, size + 1):
        if x == 4:
            rand_var.append((x ** 2,p4))
        else:
            rand_var.append((x ** 2,p1_3))

    print("#2:", variance(rand_var))


# X is a random variable, a list of tuples where each tuple is (elemnts of support of X, prob of X = value)
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


q1()
q2()
