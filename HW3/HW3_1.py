from scipy.special import binom, factorial

#1a
def one_a():
    p = .75
    n = 10
    sum = 0

    for i in range(7,n+1):
        x = (binom(n,i)*(p**i)*((1-p)**(n-i)))
        sum = sum + x
        print ("Probability of",n,"choose", i,"=", x)

    print("Probability of Latouch identifying at least 7/10:",sum)


#1b
def one_b():
    n = 10
    sum = 0

    for i in range(6,-1,-1):
        x = (binom(n, i) / (2**n))
        sum = sum + x
        print("Probability of ",n,"choose",i ,"=",x)

    print("Probability of Latouch identifying at most 6/10:", sum)


one_a()
print("\nOnto Part b")
one_b()