# -*- coding:utf-8 -*-
# carete by steve at  2017 / 02 / 23　19:06


import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

import time

if __name__ == '__main__':
    user_pay = np.fromfile("../Data/user_pay.bin", dtype=float)

    user_pay = user_pay.reshape(-1, 3)

    print("user pay size :", user_pay.shape)

    shop_info_file = open("../Data/shop_info.txt", mode='r', encoding='utf-8')
    shop_info_lines = shop_info_file.readlines()

    print("shop all :", len(shop_info_lines))

    sec2dayratio = 24.0 * 3600.0
    total_days = (np.max(user_pay[:, 2]) - np.min(user_pay[:, 2])) / sec2dayratio
    # first_time = np.min(user_pay[:,2])
    first_time = float(time.mktime(
        time.strptime("2015-07-01 00:00:00",
                      '%Y-%m-%d %H:%M:%S')

    ))
    print("total days ", total_days)

    shop_total = np.zeros([len(shop_info_lines), int(total_days + 1)])

    for i in range(user_pay.shape[0]):
        shop_total[int(user_pay[i, 1] - 1), int((user_pay[
                                                     i, 2] - first_time) / sec2dayratio)] += 1  # shop_total[user_pay[i,1]-1,int((user_pay[i,2]-first_time)/sec2dayratio)] + 1

    shop_total.tofile("../data/tmp_shop_total.bin")
    np.savetxt("shop_total.txt",shop_total[:,1:])

    plt.figure(1)
    plt.grid(True)

    for i in range(20):
        plt.plot(shop_total[i, :])
    plt.show()
    # plt.savefig("1.fig")
