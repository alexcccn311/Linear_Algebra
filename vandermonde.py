# 作者：Alex
# 2024/8/30 上午3:05
import numpy as np


A = np.array([
    [1, 1, 1, 1],
    [2, 3, -1, 1],
    [4, 9, 1, 1],
    [8, 27, -1, 1]
])


def vandermonde_calculation(matrix, vandermonde_rows, row):
    if vandermonde_rows:
        x = 1
        for y in range(row):
            if matrix[0, y] != 1:
                x = 0
                break
        result = 1
        for y in range(1, row):
            for i in range(y):
                result = result * (matrix[x, y] - matrix[x, i])
    else:
        y = 1
        for x in range(row):
            if matrix[x, 0] != 1:
                y = 0
                break
        result = 1
        for x in range(1, row):
            for i in range(x):
                result = result * (matrix[x, y] - matrix[i, y])
    return result


def vandermonde_test(matrix, row):
    vandermonde_row, vandermonde_col = True, True
    for y in range(row):
        if matrix[0, y] == 0:
            for x in range(row):
                if matrix[x, y] != 0:
                    vandermonde_row = False
                    break
        else:
            z = matrix[1, y] / matrix[0, y]
            for x in range(row - 1):
                if z * matrix[x, y] != matrix[x + 1, y]:
                    vandermonde_row = False
                    break
        if not vandermonde_row:
            break
    for x in range(row):
        if matrix[x, 0] == 0:
            for y in range(row):
                if matrix[x, y] != 0:
                    vandermonde_col = False
                    break
        else:
            z = matrix[x, 1] / matrix[x, 0]
            for y in range(row - 1):
                if z * matrix[x, y] != matrix[x, y + 1]:
                    vandermonde_col = False
                    break
        if not vandermonde_col:
            break

    if vandermonde_row or vandermonde_col:
        result = vandermonde_calculation(matrix, vandermonde_row, row)
        print(f'The Determinant is Vandermonde Determinant, Determinant(A)={result}')
        return True
    else:
        print('The Determinant is not Vandermonde Determinant')
        return False


if __name__ == '__main__':
    rows, cols = A.shape
    if rows != cols:
        print('The matrix is not determinant')
    else:
        vandermonde_test(A, rows)
