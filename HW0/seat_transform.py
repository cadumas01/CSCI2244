def transform(x):
    return (12*x + 5) % 18


if __name__ == "__main__":
    seq = []
    n = 20
    x = 2
    for i in range(n):
        seq.append(x)
        x = transform(x)


    print(seq)