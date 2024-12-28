import numpy as np

v = np.array([1, 2, 3]) 
v_transpose = v.reshape(-1, 1)  

A = np.array([[1, 2], [3, 4]])

A_transpose = A.T

B = np.array([[1 + 1j, 2], [3, 4 - 1j]])

B_conjugate_transpose = B.conj().T

print("Vector (row):", v)
print("Vector (column):\n", v_transpose)
print("Matrix A:\n", A)
print("Transpose of A:\n", A_transpose)
print("Complex Matrix B:\n", B)
print("Conjugate Transpose of B:\n", B_conjugate_transpose)
