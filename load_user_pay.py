#! /usr/bin/env python
# -*- coding: utf-8 -*-
# --- create by :load_user_pay at : 17-2-20  下午4:10

import numpy as np
from array import array

import time

if __name__ == '__main__':
    user_pay = open("user_view.txt")

    pay_buf = array("d")

    line = user_pay.readline()

    while line:

        print(line)

        pay_buf.append(float(line.split(',')[0]))
        pay_buf.append(float(line.split(',')[1]))
        # print(line.split(',')[2])
        # print(time.mktime(time.strptime(line.split(',')[2].split('\n')[0],'%Y-%m-%d %H:%M:%S')))
        pay_buf.append(float(time.mktime(time.strptime(line.split(',')[2].split('\n')[0],'%Y-%m-%d %H:%M:%S'))))




        line = user_pay.readline()

    pay_np_array = np.frombuffer(pay_buf,dtype=np.float).reshape(-1,3)

    print(pay_np_array.shape)
    pay_np_array.tofile('user_view.bin')