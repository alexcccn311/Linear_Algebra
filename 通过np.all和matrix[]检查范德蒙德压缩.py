# 作者：Alex
# 2024/8/30 上午9:58
import numpy as np


def calculate_determinant(values):
    result = 1
    n = len(values)
    for i in range(1, n):
        for j in range(i):
            result *= (values[i] - values[j])
    return result


def vandermonde_calculation(matrix, vandermonde_rows, row):
    if vandermonde_rows:
        row_index = 0 if np.all(matrix[0, :] == 1) else 1
        values = matrix[row_index, :]
    else:
        col_index = 0 if np.all(matrix[:, 0] == 1) else 1
        values = matrix[:, col_index]

    return calculate_determinant(values)


def vandermonde_test(matrix, row):
    vandermonde_row = True
    vandermonde_col = True

    # 检查行是否为范德蒙德形式
    for y in range(row):
        if matrix[0, y] == 0 or not np.all(matrix[1:, y] == matrix[1:, y] * matrix[1:, 0] / matrix[0, y]):
            vandermonde_row = False
            break

    # 检查列是否为范德蒙德形式
    for x in range(row):
        if matrix[x, 0] == 0 or not np.all(matrix[x, 1:] == matrix[x, 1:] * matrix[1, 1:] / matrix[x, 0]):
            vandermonde_col = False
            break

    if vandermonde_row or vandermonde_col:
        result = vandermonde_calculation(matrix, vandermonde_row, row)
        print(f'The Determinant is Vandermonde Determinant, Determinant(A)={result}')
        return True
    else:
        print('The Determinant is not Vandermonde Determinant')
        return False


if __name__ == '__main__':
    A = np.array([
        [1, 1, 1, 1],
        [2, 3, -1, 1],
        [4, 9, 1, 1],
        [8, 27, -1, 1]
    ])
    rows, cols = A.shape
    if rows != cols:
        print('The matrix is not square and cannot have a determinant.')
    else:
        vandermonde_test(A, rows)
