import numpy as np


# 半径1の円の面積をモンテカルロ法により求めることで、円周率の近似値を求める
def calc_pi_by_mc(iter: int = 1000):
    n_in = 0
    for i in range(iter):
        x, y = np.random.rand(), np.random.rand() # 0と1の間の一様乱数
        if x**2 + y**2 < 1:
            n_in += 1
    return (n_in / iter) * 4
