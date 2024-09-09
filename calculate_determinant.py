# 作者：Alex
# 2024/8/30 上午3:05
import numpy as np
from Row_column_multiples_check import determinant_same_cols_rows
from vandermonde import vandermonde_test
from calculation_laplace import laplace_expansion

A = np.array([
    [1, 1, 1, 1],
    [2, 3, -1, 6],
    [32, 14, 21, 1],
    [8, 27, -1, 1]
])


def quick_calculate_determinant_value(matrix):
    rows, cols = matrix.shape
    if rows != cols:
        print('The matrix is not determinant')
        return False
    else:
        if determinant_same_cols_rows(matrix):
            determinant_value = 0
            return determinant_value
        else:
            determinant_value = vandermonde_test(matrix)
            if type(determinant_value) is not bool:
                return determinant_value
            else:
                determinant_value = laplace_expansion(matrix)
                return determinant_value


if __name__ == '__main__':
    print(f'the determinant value = {quick_calculate_determinant_value(A)}')
