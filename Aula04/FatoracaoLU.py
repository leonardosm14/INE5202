import numpy as np
import scipy as sp


A = np.array([[1, 1, 0, 3], [2, 1, -1, 1], [3, -1, -1, 2], [-1, 2, 3, -1]])
b = np.array([1,1,-3,4])

P, L, U = sp.linalg.lu(A)

bm = np.dot(np.transpose(P), b)

print(bm)