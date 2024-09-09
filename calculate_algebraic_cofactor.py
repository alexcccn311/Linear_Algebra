# 作者：Alex
# 2024/9/7 下午4:58
import numpy as np
from calculation_laplace import laplace_expansion


def algebraic_cofactor(matrix, x, y):
    sub_matrix = np.delete(np.delete(matrix, x, axis=0), y, axis=1)
    result = -1 ** (x + y) * laplace_expansion(sub_matrix)
    return result

