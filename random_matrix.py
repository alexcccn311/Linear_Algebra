# 作者：Alex
# 2024/9/23 下午5:57
import numpy as np

def random_matrix(a, b, c, d=None, e=None):
    # 如果 a 是 'rand'，生成b行c列的矩阵，所有元素0-1之间的均匀分布随机矩阵
    if a == 'rand':
        return np.random.rand(b, c)
    # 如果 a 是 'randint'，生成b行c列的随机整数矩阵，所有元素为d-e之间的随机整数
    elif a == 'randint':
        if d is None or e is None:
            raise ValueError("randint 需要指定 d 和 e 的范围")
        return np.random.randint(d, e, size=(b, c))
    # 如果 a 是 'randn'，生成b行c列的矩阵，所有元素均值为 0，标准差为 1 的标准正态分布随机数
    elif a == 'randn':
        return np.random.randn(b, c)
    # 如果 a 是 'uniform'，生成b行c列的矩阵，所有元素为d-e之间的随机数
    elif a == 'uniform':
        if d is None or e is None:
            raise ValueError("uniform 需要指定 d 和 e 的范围")
        return np.random.uniform(d, e, size=(b, c))
    # 如果 a 是 'normal'，生成b行c列的矩阵，所有元素服从均值为 d，标准差为 e 的正态分布
    elif a == 'normal':
        if d is None or e is None:
            raise ValueError("normal 需要指定 d 和 e")
        return np.random.normal(d, e, size=(b, c))
    # 如果 a 是 'choice'，生成b行c列的矩阵，所有元素为d或者e
    elif a == 'choice':
        if d is None or e is None:
            raise ValueError("choice 需要指定 d 和 e")
        return np.random.choice([d, e], size=(b, c))
    else:
        raise ValueError(f"无效的生成类型: {a}")
if __name__ == '__main__':
    # 测试代码
    print("rand 矩阵:")
    print(random_matrix('rand', 2, 3))

    print("\nrandint 矩阵:")
    print(random_matrix('randint', 2, 3, 10, 20))

    print("\nrandn 矩阵:")
    print(random_matrix('randn', 2, 3))

    print("\nuniform 矩阵:")
    print(random_matrix('uniform', 2, 3, 0, 1))

    print("\nnormal 矩阵:")
    print(random_matrix('normal', 2, 3, 5, 2))

    print("\nchoice 矩阵:")
    print(random_matrix('choice', 2, 3, 0, 1))
