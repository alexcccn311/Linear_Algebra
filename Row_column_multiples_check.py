# 作者：Alex
# 2024/8/30 上午3:05
import numpy as np


def determinant_same_cols_rows(matrix):
    same_row, same_col = (False, False), (False, False)
    row, col = matrix.shape
    xz, iz, zy, zk = -1, -1, -1, -1
    for x in range(row):
        for i in range(x + 1, row):
            for index_i, value in enumerate(matrix[i, :]):
                if value != 0:
                    iz = index_i
                    break
            for index_x, value in enumerate(matrix[x, :]):
                if value != 0:
                    xz = index_x
                    break
            if xz != iz or iz == -1:
                continue
            z = matrix[x, xz]/matrix[i, iz]
            for j in range(iz, row):
                if not np.isclose(z*matrix[i, j], matrix[x, j]):
                    break
                elif j == row - 1:
                    same_row = (x, i)
                    break
            if same_row != (False, False):
                break
        if same_row != (False, False):
            break
    for y in range(row):
        for k in range(y + 1, row):
            for index_k, value in enumerate(matrix[:, k]):
                if value != 0:
                    zk = index_k
                    break
            for index_y, value in enumerate(matrix[:, y]):
                if value != 0:
                    zy = index_y
                    break
            if zk != zy or zk == -1:
                continue
            z = matrix[zy, y]/matrix[zk, k]
            for s in range(row):
                if not np.isclose(z * matrix[s, k], matrix[s, y]):
                    break
                elif s == row - 1:
                    same_col = (y, k)
                    break
            if same_col != (False, False):
                break
        if same_col != (False, False):
            break
    if same_col != (False, False) or same_row != (False, False):
        return True
    else:
        return False


if __name__ == '__main__':
    A = np.array([
        [1, 2, 3, 4],
        [0, 5, -1, 3],
        [0, 0, 6, 32],
        [3, 6, 9, 12]
    ])

    rows, cols = A.shape
    if rows != cols:
        print('The matrix is not determinant')
    determinant_same_cols_rows(A)

