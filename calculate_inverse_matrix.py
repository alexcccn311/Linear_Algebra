# 作者：Alex
# 2024/9/9 下午12:26
import numpy as np
from calculate_determinant import quick_calculate_determinant_value
from calculate_adjugate_matrix import adjugate_matrix

A = np.array([
    [1, 1, 1, 1],
    [2, 3, -1, 1],
    [4, 9, 1, 1],
    [8, 27, -1, 1]
])


def inverse_matrix(matrix):
    rows, cols = matrix.shape
    if cols != rows:
        raise ValueError("The input matrix must be square to have an inverse.")

    value_determinant = quick_calculate_determinant_value(matrix)
    if value_determinant == 0:
        raise ValueError("The input matrix does not have an inverse because it is singular (determinant is zero).")

    result_matrix = adjugate_matrix(matrix) / value_determinant
    return result_matrix


if __name__ == '__main__':
    print(inverse_matrix(A))