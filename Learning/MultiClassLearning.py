# -*- coding:utf-8 -*-
# carete by steve at  2017 / 02 / 23　20:28


import numpy as np
import scipy as sp

import matplotlib.pyplot as plt

if __name__ == '__main__':
    shop_lable = np.fromfile("../Data/tmp_shop_lable.bin", dtype=int)
    src_data = np.fromfile("../Data/tmp_shop_total.bin", dtype=float)
    print(shop_lable)
    types_num = np.zeros(int(np.max(shop_lable)))
    for i in range(shop_lable.shape[0]):
        types_num[int(shop_lable[i])-1] += 1

    X_list = list()
    Y_list = list()
    index_list = list()

    time_step = 14  # number of input data.

    for i in range(np.max(shop_lable)):
        X_list.append(np.zeros([
            int(src_data.shape[1] - 1 - time_step) * types_num[i],
            int(time_step)
        ]))
        Y_list.append(np.zeros([int(src_data.shap[1] - 1 - time_step) *
                                types_num[i]
                                   , 1]))
        index_list.append(0)

    for i in range()


