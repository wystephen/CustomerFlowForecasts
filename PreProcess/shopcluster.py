# -*- coding:utf-8 -*-
# carete by steve at  2017 / 02 / 23　19:40

import numpy as np
import scipy as sp

import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.cluster import dbscan
if __name__ == '__main__':
    X = np.fromfile("../Data/tmp_shop_total.bin",dtype=float)
    X=X.reshape(2000,-1)

    t_X = X[:,-101:]
    #t_X = t_X / np.sum(t_X,1).reshape(2000,1)
    types_num = 100
    kmeans = KMeans(n_clusters=types_num,random_state=0).fit(t_X)
    cluster_result = kmeans.labels_
    Dbscan = dbscan(t_X)
    print(Dbscan)

    subclass_total_num = np.zeros([types_num])
    for i in range(len(cluster_result)):
        subclass_total_num[cluster_result[i]] +=1
    subclass_total_num.sort()

    shop_lable = np.zeros([2000])
    shop_lable = cluster_result

    shop_lable.tofile("../Data/tmp_shop_lable.bin")


    plt.figure(2)
    plt.plot(subclass_total_num,'*r-')

    plt.figure(1)
    plt.grid(True)
    plt.plot(kmeans.labels_,'+r')
    plt.show()