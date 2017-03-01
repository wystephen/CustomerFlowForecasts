# -*- coding:utf-8 -*-
# carete by steve at  2017 / 02 / 28　21:19

import numpy as np
import scipy as sp

import matplotlib.pyplot as plt

from sklearn.svm import SVR,NuSVR,LinearSVR
from sklearn.ensemble import RandomForestRegressor


from evaluation import evaluation

if __name__ == '__main__':
    shop_data = np.fromfile('../Data/tmp_shop_total.bin',dtype=float)
    shop_data = shop_data.reshape(2000,-1)
    np.savetxt("shop_data.txt",shop_data)


    print("shop data :",shop_data)


    weather_data = np.loadtxt("../Data/weather_array.txt")
    min_temp = np.loadtxt("../Data/min_temp_array.txt")
    max_temp = np.loadtxt("../Data/max_temp_array.txt")

    print(weather_data.shape,min_temp.shape,max_temp.shape)
    weather_data = weather_data[:,:-16]
    min_temp = min_temp[:,:-16]
    max_temp = max_temp[:,:-16]

    print(weather_data.shape,min_temp.shape,max_temp.shape)
    predict_weather = weather_data[:,-14:]
    predict_min = min_temp[:,-14:]
    predict_max = max_temp[:,-14:]
    predict_time = np.zeros([2000,14])
    for i in range(14):
        # print(1+i)
        predict_time[:,i] = i+1+shop_data.shape[1]
    print(predict_time)

    train_weather = weather_data[:,-90:-14]
    train_min = min_temp[:,-90:-14]
    train_max = max_temp[:,-90:-14]
    # train_weather = train_weather[:,:-5]

    train_time = np.zeros([2000,train_weather.shape[1]])




    for i in range(train_time.shape[1]):
        train_time[:,train_time.shape[1]-i-1]=shop_data.shape[1]-i
    train_result = shop_data[:,-train_time.shape[1]:]




    train_time = train_time[:,:-5]
    train_weather = train_weather[:,:-5]
    train_min = train_min[:,:-5]
    train_max = train_max[:,:-5]
    train_result = train_result[:,:-5]
    print (train_time)

    print(train_time.shape,train_result.shape)

    # print([train_time,train_max,train_min,train_weather])
    # train_data_set = np.zeros(train_time)
    # train_time -= 400
    # predict_time -=400
    # train_time /= 10.0
    # predict_time /=10.0
    train_time = train_time % 7
    predict_time = predict_time % 7


    rnf_list = list()
    predict_result = np.zeros([2000,14])
    for i in range(train_time.shape[0]):
        tmp_rnf = RandomForestRegressor()
        # tmp_fnf.fix()
        tmp_X = np.zeros([train_time.shape[1],4])
        tmp_X[:,0] = train_time[i,:]
        tmp_X[:,1] = train_weather[i,:]
        tmp_X[:,2] = train_min[i,:]
        tmp_X[:,3] = train_max[i,:]
        tmp_rnf.fit(tmp_X[:-14,:],train_result[i,:-14])
        predict_result[i,:] = tmp_rnf.predict(tmp_X[-14:,:])
        rnf_list.append(tmp_rnf)

    print("predict:",predict_result)
    print("\n\n\n\n\n\n\nLoss:",evaluation.LossFunction(train_result[:,:],(predict_result[:,:])))

    result = np.zeros([2000,14])
    for i in range(len(rnf_list)):
        tmp_rnf = RandomForestRegressor()
        tmp_X = np.zeros([train_time.shape[1],4])
        tmp_X[:,0] = train_time[i,:]
        tmp_X[:,1] = train_weather[i,:]
        tmp_X[:,2] = train_min[i,:]
        tmp_X[:,3] = train_max[i,:]
        tmp_rnf.fit(tmp_X[:,:],train_result[i,:])
        pre_X = np.zeros([14,4])
        pre_X[:,0] = predict_time[i,:]
        pre_X[:,1] = predict_weather[i,:]
        pre_X[:,2] = predict_min[i,:]
        pre_X[:,3] = predict_max[i,:]
        result[i,:] = tmp_rnf.predict(pre_X)
    print(result)


    all_result = np.zeros([2000,15])
    for i in range(all_result.shape[0]):
        all_result[i,0] = i+1
        all_result[i,1:] = np.abs(result[i,:])

    plt.figure(1)
    plt.grid(True)
    plt.plot(np.mean(train_result,1),'r')
    plt.plot(np.mean(result,1),'b')
    plt.show()
    print('train result :',train_result[1,-14:])


    np.savetxt("all_result.csv",all_result,"%d",delimiter=',')













