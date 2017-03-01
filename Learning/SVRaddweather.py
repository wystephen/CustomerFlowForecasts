# -*- coding:utf-8 -*-
# carete by steve at  2017 / 02 / 28　21:19

import numpy as np
import scipy as sp

import matplotlib.pyplot as plt

if __name__ == '__main__':
    shop_data = np.fromfile('../Data/tmp_user_shop.bin',dtype=float)
    shop_data = shop_data.reshape(2000,-1)

