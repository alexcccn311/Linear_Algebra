# 作者：Alex
# 2024/9/2 上午9:46
import numpy as np

A = np.array([
    [1, 1, 1, 1, 1],
    [2, 3, -1, 1, 4],
    [4, 9, 1, 1, 16],
    [8, 27, -1, 1, 64]
])

B = np.array([
    [1, 24, 1, 17],
    [2, 5, 22, 13],
    [4, 7, 1, 12],
    [8, 31, -13, 14],
    [16, 25, 31, 24]
])


def matrix_multiplication(matrix1, matrix2):
    rows_1, cols_1 = matrix1.shape
    rows_2, cols_2 = matrix2.shape
    if cols_1 != rows_2:
        raise ValueError("Matrices must have same number of rows and columns")
    matrix3 = np.zeros((rows_1, cols_2))
    for x in range(rows_1):
        for y in range(cols_2):
            for z in range(cols_1):
                matrix3[x, y] += matrix1[x, z] * matrix2[z, y]
    return matrix3


if __name__ == "__main__":
    print(matrix_multiplication(A, B))
