# 作者：Alex
# 2024/9/20 下午10:53
import numpy as np


def inverse_matrix_gauss_jordan(matrix):
    rows, cols = matrix.shape
    if rows != cols:
        raise ValueError("The input matrix must be square to have an inverse.")

    # 构建扩展矩阵 [A | I]
    identity_matrix = np.eye(rows)
    augmented_matrix = np.hstack((matrix, identity_matrix))

    # 高斯-约当消元法，进行初等行变换
    for i in range(rows):
        # 1. 找到主元，并将主元行归一化
        pivot = augmented_matrix[i, i]
        if pivot == 0:
            # 处理行交换的情况，如果主元为0，找到下面的非零行进行交换
            for j in range(i + 1, rows):
                if augmented_matrix[j, i] != 0:
                    augmented_matrix[[i, j]] = augmented_matrix[[j, i]]
                    # augmented_matrix[[i, j]]为选取第i行和第j行的所有元素
                    # augmented_matrix[[j, i]]为选取第j行和第i行的所有元素
                    break
            pivot = augmented_matrix[i, i]
            if pivot == 0:
                raise ValueError("The matrix is singular and cannot be inverted.")

        # 将主元行除以主元，使主元为 1
        augmented_matrix[i] = augmented_matrix[i] / pivot

        # 2. 对其他行进行消元，使主元列的其他元素为 0
        for j in range(rows):
            if j != i:
                factor = augmented_matrix[j, i]
                augmented_matrix[j] -= factor * augmented_matrix[i]

    # 取出右边部分作为逆矩阵
    inverse_matrix = augmented_matrix[:, cols:]

    return inverse_matrix


if __name__ == '__main__':
    A = np.array([
        [1, 1, 1, 1],
        [2, 3, -1, 1],
        [4, 9, 1, 1],
        [8, 27, -1, 1]
    ])

    try:
        inv_A = inverse_matrix_gauss_jordan(A)
        print("Inverse matrix:\n", inv_A)
    except ValueError as e:
        print(e)
