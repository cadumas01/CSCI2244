import numpy as np

# Like Matlab but 0 index based not 1 based

# arrays are like matlab matrix
a = np.array([[1,2,3],[4,5,6]]) # 2 by 3 array
b = np.array([[3,4],[5,6],[-10,-3]]) # 3 by 2 array

# arrays can be transformed element wise


# use @ for matrix (array) multiplication
print("a: \n", a)
print("\n")
print("b: \n", b)
print("\n")

print("b*2: \n", b*2)
print('\n')

print(a@b)
print("\n")

print(a[:,0]) # 0th col
print(a[0,:]) # 0th row
print("\n")

# Indexing from the end (rather than the beginning)
print(b[-2,-1]) # prints the element in the second to last row and the last col of b
print("\n")

# boolean array
print(b > 2) # boolean array, each element is compared against this condition
print("\n")

# boolean indexing
print(b[b > 2]) # only prints elements that meet this condition
print("\n")
print(np.where(b>2,b,-1)) # for each in b, if that element is greater than 2, then use b else use -1

