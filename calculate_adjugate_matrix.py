# 作者：Alex
# 2024/9/7 下午4:39
import numpy as np
from calculate_algebraic_cofactor import algebraic_cofactor
A = np.array([
    [2, -1, 0],
    [1, 3, 4],
    [0, -2, 5],
])


def adjugate_matrix(matrix):
    rows, cols = matrix.shape
    if rows != cols:
        raise ValueError("The input matrix must be square to calculate its adjugate matrix.")
    result_matrix = np.zeros(shape=(rows, cols))
    for x in range(rows):
        for y in range(cols):
            result_matrix[y, x] = algebraic_cofactor(matrix, x, y)
    return result_matrix


if __name__ == '__main__':
    print(adjugate_matrix(A))
    print(adjugate_matrix(adjugate_matrix(A)))
