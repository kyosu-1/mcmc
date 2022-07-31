import numpy as np


# 半径1の円の面積をモンテカルロ法により求めることで、円周率の近似値を求める
def py_mc(iter: int = 1000):
    n_in = 0
    for i in range(iter):
        x, y = np.random.uniform(0, 1), np.random.uniform(0, 1) # 0と1の間の一様乱数
        if x**2 + y**2 < 1:
            n_in += 1
    return (n_in / iter) * 4


if __name__ == '__main__':
    print(py_mc(10000))
    print(np.pi)
