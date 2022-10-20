import numpy as np

a= 4
b= 5
c =6

A = np.array([[1, 2, 3], [a, b, c]])
B = np.array([[7, 8], [-9, 10], [11, -12]])
C = A.dot(B)
print(A)
print(B)