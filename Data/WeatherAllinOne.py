# -*- coding:utf-8 -*-
# carete by steve at  2017 / 02 / 25　23:09

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

import os
import time
import os


class ExtentData():
    def __init__(self, file_name="weather_all.csv"):
        weather_file = open(file_name, encoding='utf-8')
        self.weather_dict = dict()
        self.temp_min_dict = dict()
        self.temp_max_dict = dict()

        city_name = "Not"

        self.day_num = 0
        weather_list = list()
        temp_min_list = list()
        temp_max_list = list()
        tmp_counter = 0
        weather_file_list = weather_file.readlines()
        for line in weather_file_list:
            tmp_counter+=1
            if False:
                next(line)
            else:
                if city_name != line.split(',')[0] :#or
                    self.weather_dict.update(dict({
                        city_name: np.asarray(weather_list, dtype=int)
                    }))
                    self.temp_min_dict.update(dict(
                        {
                            city_name: np.asarray(temp_min_list, dtype=int)
                        }
                    )
                    )
                    self.temp_max_dict.update(dict({
                        city_name: np.asarray(temp_max_list, dtype=int)
                    }))
                    print(len(weather_list), len(temp_min_list), len(temp_max_list))
                    self.day_num = len(weather_list)
                    weather_list.clear()
                    temp_min_list.clear()
                    temp_max_list.clear()
                    # print("weather :",self.weather_dict[city_name])
                    # print("min,max:",self.temp_min_dict[city_name])
                    # print("max:",self.temp_max_dict[city_name])
                    city_name = line.split(',')[0]
                elif tmp_counter == len(weather_file_list):
                    # weather
                    weather_list.append(self.str2int_weather(line.split(',')[4]))

                    # min max
                    temp_min_list.append(int(line.split(',')[3]))
                    temp_max_list.append(int(line.split(',')[2]))

                    self.weather_dict.update(dict({
                        city_name: np.asarray(weather_list, dtype=int)
                    }))
                    self.temp_min_dict.update(dict(
                        {
                            city_name: np.asarray(temp_min_list, dtype=int)
                        }
                    )
                    )
                    self.temp_max_dict.update(dict({
                        city_name: np.asarray(temp_max_list, dtype=int)
                    }))
                    print(len(weather_list), len(temp_min_list), len(temp_max_list))
                else:
                    # weather
                    weather_list.append(self.str2int_weather(line.split(',')[4]))

                    # min max
                    temp_min_list.append(int(line.split(',')[3]))
                    temp_max_list.append(int(line.split(',')[2]))


    def str2int_weather(self, weather_str):
        if "雪" in weather_str:
            return 0
        elif "雨" in weather_str:
            return 1
        elif "阴" in weather_str or "多云" in weather_str:
            return 2
        elif "晴" in weather_str:
            return 3
        else:
            return 4

    def generator_file(self, shop_file="shop_info.txt"):
        shops = open(shop_file, encoding='utf-8')
        shop_list = shops.readlines()
        weather_array = np.zeros([len(shop_list), self.day_num])
        min_array = np.zeros([len(shop_list), self.day_num])
        max_array = np.zeros([len(shop_list), self.day_num])
        index = 0

        for the_line in shop_list:
            print(the_line.split(',')[1])
            weather_array[index, :] = self.weather_dict[the_line.split(',')[1]]
            min_array[index, :] = self.temp_min_dict[the_line.split(',')[1]]
            max_array[index, :] = self.temp_max_dict[the_line.split(',')[1]]
            index += 1

        np.savetxt("min_temp_array.txt", min_array)
        np.savetxt("max_temp_array.txt", max_array)
        np.savetxt("weather_array.txt", weather_array)
        print(max_array.shape, min_array.shape, weather_array.shape)


if __name__ == '__main__':
    ed = ExtentData()
    ed.generator_file()
