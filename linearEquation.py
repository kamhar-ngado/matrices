import numpy as np 
import math
# SPLDV
# 20x + 10y = 350
# 17x + 22y = 500
# A = np.array([[20, 10], [17, 22]])
# B = np.array([350, 500])
# X = np.linalg.solve(A,B)
# print(X)


# 4x + 3y + 2z = 25
# -2x + 2y + 3z = -10
# 3x - 5y + 2z = -4
# what is the value of [x, y, z] + [1, 2, 3] in python

# A = np.array([[4, 3, 2], [-2, 2, 3], [3, -5, 2]])
# B = np.array([25, -10, -4])
# C = np.linalg.solve(A,B)
# print(C)

A = np.array([[4, 3, 2], [-2, 2, 3], [3, -5, 2 ]])
B = np.array([25, -10, 4])
C = np.linalg.solve(A, B)
print((C))