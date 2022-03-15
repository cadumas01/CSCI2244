import math

from scipy.special import binom, factorial

#1
p = .0005
n = 300
prob1 = 0
k=2

for k in range(0,k):
    prob1 += binom(n, k) * (p**k)*(1-p)**(n-k)


print("1:", prob1)




#2
def hypergeom(v,N,k,n):
    return (binom(k,v) * binom(N-k, n-v))/ (binom(N,n))

prob2 = 0
N = 27
k = 6
n = 7
for v in range (0,2):
    prob2 += hypergeom(v, N, k, n)

print("2:", prob2)


#3

def geometric(p,k):
    return (1-p)**(k-1) * p

prob3 = 0

p = .47
for k in range(1,3):
    prob3 += geometric(p,k)

print("3:", 1 - prob3)


# 4

def poisson(lambd,k):
    return (lambd**k) *(math.e**(-lambd)) / factorial(k)


p = .003
n = 500
prob4 = 0
lambd = n*p

for k in range (0,2):
    prob4 += poisson(lambd, k)


print("4:", prob4)

# 5

print("5", (5/15)*(8/13)*(9/19)+(5/15)*(5/13)*(10/19)+(10/15)*(8/13)*(10/19) )