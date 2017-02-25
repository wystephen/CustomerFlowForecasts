# -*- coding:utf-8 -*-
# carete by steve at  2017 / 02 / 24　19:54

import numpy as np
import scipy as sp

import matplotlib.pyplot as plt

def LossFunction(predict_data,ground_truth):

    if(predict_data.shape == ground_truth.shape):
        return 1.0/(predict_data.shape[0]*predict_data.shape[1])*np.sum(np.abs((predict_data-ground_truth)/(predict_data+ground_truth+1e-30)))

    else:
        print("ERROR predict shape is :",predict_data.shape,"ground truth shape is :" ,ground_truth.shape)
        return 1.0



if __name__ == '__main__':
    src_data = np.fromfile("../Data/tmp_shop_total.bin",dtype=float)
    src_data = src_data.reshape(2000,-1)
    print(src_data)
    print(src_data.shape)
    print("sum src_data:" , np.sum(src_data))
    print("loss add normal noise: ",LossFunction(src_data,src_data+np.random.normal(0.0,0.000000001,src_data.shape)))
    print("loss add 1 :",LossFunction(src_data,src_data))
    print("same :",LossFunction(src_data,src_data))
    plt.figure(1)
    plt.imshow(src_data)
    plt.show()


