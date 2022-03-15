
def p_i(n, i):
    return 1 - ((1 - ((n - i + 1) / n)) ** 3)

def main():
    sum = 0
    n = 18
    for i in range(1, n + 1):
        sum += 1 / p_i(n, i)

    print(sum)


main()


