# 作者：Alex
# 2024/9/9 下午12:26
import numpy as np
from calculate_determinant import determinant_value
from calculate_adjugate_matrix import adjugate_matrix


def inverse_matrix(matrix):
    rows, cols = matrix.shape
    if cols != rows:
        raise ValueError("The input matrix must be square to have an inverse.")

    det_value = determinant_value(matrix)
    if det_value == 0:
        raise ValueError("The matrix is not invertible because its determinant is zero.")

    result_matrix = adjugate_matrix(matrix) / det_value
    return result_matrix


if __name__ == '__main__':
    A = np.array([
        [1, 1, 1, 1],
        [2, 3, -1, 1],
        [4, 9, 1, 1],
        [8, 27, -1, 1]
    ])

    print(inverse_matrix(A))
