import numpy as np

def gauss_elimination(a, b):
 
    n = len(b)

    for i in range(n):
        max_row = i + np.argmax(abs(a[i:, i]))
        if max_row != i:
            a[[i, max_row]] = a[[max_row, i]]
            b[[i, max_row]] = b[[max_row, i]]

        for j in range(i + 1, n):
            factor = a[j, i] / a[i, i]
            a[j, i:] -= factor * a[i, i:]
            b[j] -= factor * b[i]

    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - np.dot(a[i, i + 1:], x[i + 1:])) / a[i, i]

    return x

A = np.array([[2, 1, -1], [-3, -1, 2], [-2, 1, 2]], dtype=float)
b = np.array([8, -11, -3], dtype=float)

solution_non_homogeneous = gauss_elimination(A.copy(), b.copy())
print("Solution for the non-homogeneous system:", solution_non_homogeneous)

A_homogeneous = np.array([[2, 1, -1], [-3, -1, 2], [-2, 1, 2]], dtype=float)
b_homogeneous = np.zeros(3, dtype=float)

solution_homogeneous = gauss_elimination(A_homogeneous.copy(), b_homogeneous.copy())
print("Solution for the homogeneous system:", solution_homogeneous)

