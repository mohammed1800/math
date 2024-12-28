import numpy as np

def is_linearly_dependent(vectors):
    if not vectors:
        return None
    n = len(vectors[0])
    for v in vectors:
        if len(v) != n:
            return None
    matrix = np.array(vectors).T
    rank = np.linalg.matrix_rank(matrix)
    return rank < len(vectors)

def linear_combination(vectors, coefficients):
    if len(vectors) != len(coefficients):
        return None
    if not vectors:
        return np.array([])
    n = len(vectors[0])
    for v in vectors:
        if len(v) != n:
            return None
    linear_comb = np.zeros(n)
    for i in range(len(vectors)):
        linear_comb += coefficients[i] * vectors[i]
    return linear_comb

def transition_matrix(basis1, basis2):
    if len(basis1) != len(basis2):
        return None
    n = len(basis1[0])
    for b in basis1+basis2:
        if len(b) != n:
            return None
    matrix1 = np.array(basis1).T
    matrix2 = np.array(basis2).T
    if np.linalg.matrix_rank(matrix1) != n or np.linalg.matrix_rank(matrix2) != n:
      return None
    return np.linalg.solve(matrix2, matrix1)

v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
v3 = np.array([7, 8, 9])
v4 = np.array([1, 0])
v5 = np.array([0, 1])

vectors1 = [v1, v2, v3]
vectors2 = [v4, v5]

print("Vectors 1 Linearly Dependent:", is_linearly_dependent(vectors1))
print("Vectors 2 Linearly Dependent:", is_linearly_dependent(vectors2))

coeffs = [2, -1, 0.5]
lin_comb = linear_combination(vectors1, coeffs)
print("Linear Combination:", lin_comb)

basis1 = [np.array([1, 0]), np.array([1, 1])]
basis2 = [np.array([1, 1]), np.array([0, 1])]
trans_mat = transition_matrix(basis1, basis2)

if trans_mat is not None:
    print("Transition Matrix:\n", trans_mat)
else:
    print("Could not compute transition matrix. Check input.")

basis3 = [np.array([1, 0]), np.array([2,0])]
trans_mat2 = transition_matrix(basis1, basis3)
if trans_mat2 is not None:
    print("Transition Matrix:\n", trans_mat2)
else:
    print("Could not compute transition matrix. Check input. Basis 3 is not a basis")
