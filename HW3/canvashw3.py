# We can import code from scipy to calculate binomial coefficients and
# factorials.
from scipy.special import binom, factorial
# binom(n, k) computes "n choose k":
#print(binom(3, 1))
# factorial(n) computes n!
#print("5! =", factorial(5))

#3
print((26 ** 5) * (10 ** 5))

#4
print(binom(13,3) * binom(6,4))

#
print(factorial(6) / factorial(6-4))