import numpy as np

def gram_schmidt_orthogonalization(vectors):
    orthogonal_basis = []
    orthonormal_basis = []

    for v in vectors:
        w = v - np.sum([np.dot(v, u) / np.dot(u, u) * u for u in orthogonal_basis], axis=0)
        orthogonal_basis.append(w)

        norm = np.linalg.norm(w)
        if norm == 0:
            orthonormal_basis.append(np.zeros_like(w))
        else:
            orthonormal_basis.append(w / norm)

    return orthonormal_basis

vectors = [np.array([1, 1, 0]), np.array([1, 0, 1]), np.array([0, 1, 1])]

orthonormal_basis = gram_schmidt_orthogonalization(vectors)

print("Orthonormal basis:")
for v in orthonormal_basis:
    print(v)
