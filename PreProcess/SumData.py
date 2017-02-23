# -*- coding:utf-8 -*-
# carete by steve at  2017 / 02 / 23　19:06


import numpy as np
import scipy as sp
import matplotlib.pyplot as plt


if __name__ == '__main__':
    user_pay = np.fromfile("../Data/user_pay.bin",dtype=float)

    user_pay = user_pay.reshape(-1,3)

    print("user pay size :" , user_pay.shape)


