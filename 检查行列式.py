# 作者：Alex
# 2024/8/30 上午3:05
import numpy as np
from Row_column_multiples_check import determinant_same_cols_rows
from vandermonde import vandermonde_test

A = np.array([
    [1, 1, 1, 1],
    [2, 3, -1, 1],
    [4, 9, 1, 1],
    [8, 27, -1, 1]
])

if __name__ == '__main__':
    rows, cols = A.shape
    if rows != cols:
        print('The matrix is not determinant')
    else:
        if not determinant_same_cols_rows(A, rows):
            vandermonde_test(A, rows)
