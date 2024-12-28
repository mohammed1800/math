import numpy as np
from scipy.linalg import null_space, orth

def basis_of_matrix_space(matrix):
 
    col_basis = orth(matrix.T)

    null_basis = null_space(matrix)

    row_basis = orth(matrix)

    left_null_basis = null_space(matrix.T)

    return col_basis, null_basis, row_basis, left_null_basis
