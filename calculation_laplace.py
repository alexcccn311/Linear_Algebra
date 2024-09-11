# 作者：Alex
# 2024/9/7 下午6:01
import numpy as np

A = np.array([
    [3, 4],
    [-2, 5]
])


def laplace_expansion(matrix):
    # 矩阵的行数和列数
    n = len(matrix)

    # 基本情况: 1x1 矩阵
    if n == 1:
        return matrix[0, 0]

    # 基本情况: 2x2 矩阵
    if n == 2:
        return matrix[0, 0] * matrix[1, 1] - matrix[0, 1] * matrix[1, 0]

    # 一般情况: 使用拉普拉斯展开递归计算行列式
    determinant = 0
    for j in range(n):
        # 删除第 0 行和第 j 列，得到子矩阵
        sub_matrix = np.delete(np.delete(matrix, 0, 0), j, 1)
        # 递归计算子矩阵的行列式，并累加到总的行列式中
        determinant += ((-1) ** j) * matrix[0, j] * laplace_expansion(sub_matrix)

    return determinant


if __name__ == '__main__':
    print(laplace_expansion(A))
