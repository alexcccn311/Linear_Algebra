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
    cols, rows = np.shape(np.matrix)
    if cols != rows or quick_calculate_determinant_value(matrix) == 0:
        raise ValueError("The input matrix don't have inverse matrix.")
    result_matrix = adjugate_matrix(matrix) / quick_calculate_determinant_value(matrix)
    return result_matrix


if __name__ == '__main__':
    print(inverse_matrix(A))
