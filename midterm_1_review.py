import math

from scipy.special import binom, factorial
from scipy.stats import binom as binomial


def hyper_geom(N,k,n,v):
    return binom(k,v)*binom(N-k,n-v)/binom(N,n)


def geom(p,k):
    return ((1-p)**(k-1))*(p)


def poisson(k, lambd):
    return (lambd ** k)*(math.e**(-1*lambd))/factorial(k)

# 4
print("#4:", (9/18)*(7/15)*(5/14)+(9/18)*(8/15)*(5/14)+(9/18)*(7/15)*(9/14))

# 6
print("#6:", (26**5)*(10**5))

# 7
print("#7:", binom(10, 4)*binom(5, 2))

# 8
print("#8:", factorial(17)/factorial(12))

# 9
print("#9:",(.9*.009)/(.9*.009 + .1*(1-.009)))

# 10
print("#10:", binomial.cdf(n=200, p=.01,k=2))

# 11
p_11 = 0
for i in range(0,2):
    p_11 += hyper_geom(28,4,7,i)
print("#11:",p_11)

# 12
p_12 = 0
for k in range(1,3):
    p_12 += geom(.45,k)
p_12 = 1 - p_12
print("#12:", p_12)

# 13
p_13 = 0
n = 300
p = .0025
lambd = n*p
for k in range(0,2):
    p_13 += poisson(k,lambd)
p_13 = 1 - p_13
print("#13:", p_13)


