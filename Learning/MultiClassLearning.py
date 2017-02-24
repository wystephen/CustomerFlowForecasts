# -*- coding:utf-8 -*-
# carete by steve at  2017 / 02 / 23　20:28


import numpy as np
import scipy as sp

import matplotlib.pyplot as plt

import time
import timer
import timeit

from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.svm import SVR
from sklearn.cross_validation import cross_val_score

from sklearn.neural_network import MLPRegressor

if __name__ == '__main__':
    start_time = time.localtime()
    shop_lable = np.fromfile("../Data/tmp_shop_lable.bin", dtype=int)
    src_data = np.fromfile("../Data/tmp_shop_total.bin", dtype=float)
    src_data = src_data.reshape(2000, -1)
    src_data = src_data[:, 100:]
    print(shop_lable)
    types_num = np.zeros(int(np.max(shop_lable) + 1))
    for i in range(shop_lable.shape[0]):
        types_num[int(shop_lable[i])] += 1

    X_list = list()
    Y_list = list()
    index_list = list()
    Model_list = list()

    time_step = 35  # number of input data.
    result_step = 14  # number of output data

    for i in range(np.max(shop_lable) + 1):
        print(types_num[i])
        X_list.append(np.zeros([
            int(src_data.shape[1] - result_step - time_step) *
            int(types_num[i]),
            int(time_step)
        ]))
        Y_list.append(np.zeros([int(src_data.shape[1] - result_step - time_step) *
                                int(types_num[i]),
                                int(result_step)]))
        index_list.append(0)

    src_data = src_data.astype('float')
    data_mean = np.mean(src_data)
    data_std = np.std(src_data)
    src_data = (src_data-data_mean)/data_std

    for i in range(src_data.shape[0]):
        the_type = shop_lable[i]
        for j in range(int(src_data.shape[1] - result_step - time_step)):
            X_list[the_type][index_list[the_type], :] = src_data[i, j:j + time_step]
            Y_list[the_type][index_list[the_type], :] = src_data[i,
                                                        j + time_step:j + time_step + result_step]
            index_list[the_type] += 1

    for tindex in range(len(X_list)):
        Y_list[tindex].reshape(-1)
        print(X_list[tindex].shape, " ", Y_list[tindex].shape)
        # reg = GradientBoostingRegressor()
        # if(types_num[tindex]<np.mean(types_num)/2.0):
        #     reg = RandomForestRegressor()
        # else:
        #     reg = SVR()
        reg = MLPRegressor(hidden_layer_sizes=(time_step * 2, time_step,))

        reg.fit(X_list[tindex],
                Y_list[tindex])
        print(cross_val_score(reg, X_list[tindex], Y_list[tindex]))
        Model_list.append(reg)

    estimate_result = np.zeros([2000, 15])
    if result_step == 1:

        for i in range(2000):
            print(i)
            label = shop_lable[i]
            input_data = src_data[i, -time_step:]
            estimate_result[i, 0] = i + 1
            for j in range(14):
                estimate_result[i, j + 1] = Model_list[label].predict(input_data).reshape(-1)
                input_data[:time_step - 1] = input_data[1:]
                input_data[-1] = estimate_result[i, j]
    else:
        for i in range(2000):
            print(i)
            label = shop_lable[i]
            input_data = src_data[i, -time_step:]
            estimate_result[i, 0] = i + 1
            estimate_result[i, 1:] = Model_list[label].predict(input_data)

    estimate_result[:, 1:] = data_mean+( estimate_result[:, 1:] * data_std)
    estimate_result = np.abs(estimate_result)
    src_data = src_data * data_std + data_mean

    for i in range(estimate_result.shape[0]):
        estimate_result[i, 1:] = estimate_result[i, 1:] / np.mean(estimate_result[i, 1:]) *np.mean(src_data[i, -21:])

    estimate_result.tofile("../Data/Test_result.bin")
    estimate_result = estimate_result.astype('int')

    np.savetxt("test" + str(start_time) + "'.csv",
               estimate_result, fmt='%d', delimiter=',')
    plt.figure(1)
    plt.imshow(estimate_result[:, 1:])
    plt.show()
