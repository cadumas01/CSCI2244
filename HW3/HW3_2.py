from scipy.special import binom

def main():
    p0 =.5
    p1 =.7
    n = 2
    m = 1

    while alpha(p0,m,n)  > .05 or beta(p1,m,n) > .05:
        if beta(p1,m,n) < alpha(p0,m,n):
            m += 1
        else:
            n += 1
        print("n=",n, " m=",m, " alpha=",alpha(p0,m,n), " beta=", beta(p1,m,n))


def b(n,p,k):
    return (binom(n,k)*((p)**k)*((1-p)**(n-k)))


def alpha(p,m,n):
    sum = 0
    for k in range(m,n+1):
        sum += b(n,p,k)

    return sum


def beta(p,m,n):
    return 1 - alpha(p,m,n)


main()
