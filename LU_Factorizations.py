# 作者：Alex
# 2024/9/11 下午10:36
import numpy as np


def lu_decomposition(A):
    n = A.shape[0]
    L = np.eye(n)  # 初始化L为单位矩阵
    U = np.zeros((n, n))  # 初始化U为零矩阵

    for i in range(n):
        # 计算U的第i行
        for j in range(i, n):
            U[i, j] = A[i, j] - sum(L[i, k] * U[k, j] for k in range(i))

        # 计算L的第i列
        for j in range(i + 1, n):
            L[j, i] = (A[j, i] - sum(L[j, k] * U[k, i] for k in range(i))) / U[i, i]

    return L, U


if __name__ == '__main__':
    # 示例矩阵
    A = np.array([
        [2, -1, 0],
        [1, 3, 4],
        [0, -2, 5]
    ], dtype=float)

    # 进行LU分解
    L, U = lu_decomposition(A)

    print("Matrix A:\n", A)
    print("Lower triangular matrix L:\n", L)
    print("Upper triangular matrix U:\n", U)

    # 验证 A = LU
    A_reconstructed = np.dot(L, U)
    print("Reconstructed matrix A (L * U):\n", A_reconstructed)
