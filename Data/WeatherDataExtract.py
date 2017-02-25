# -*- coding:utf-8 -*-
# carete by steve at  2017 / 02 / 25　21:59

import numpy as np
import matplotlib.pyplot as plt
import scipy
import os
import time

class WeatherDataManager:
    def __init__(self,dir_name = "Weather_Date/"):
        # print(os.listdir())
        print(os.listdir(dir_name))

        self.weather_dict = dict()
        self.temp_min_dic = dict()
        self.temp_max_dic = dict()
        # weather_type = dict()

        # Save all city name to the list
        city_list = list()
        for city_name in os.listdir(dir_name):
            if '.' not in city_name:
                city_list.append(city_name)

        # process the right city name in the city name list
        for city_name in city_list:
            save_weather_list  = list()
            save_temp_min_list = list()
            save_temp_max_list = list()
            file_list = os.listdir(dir_name+"/"+city_name)
            # print(file_list)
            for file_name in file_list:
                the_file = open(dir_name+"/"+city_name+"/"+file_name,encoding='utf-8')
                for line in the_file.readlines():
                    # print(line.split(',')[3])
                    if len(line.split(',')) >2:
                        save_weather_list.append(self.str2int_weather(line.split(',')[3]))
                        save_temp_min_list.append(int(line.split(',')[2]))
                        save_temp_max_list.append(int(line.split(',')[1]))
            self.weather_dict.update(dict({city_name:np.asarray(save_weather_list,dtype=int)}))
            self.temp_min_dic.update(dict({city_name:np.asarray(save_temp_min_list,dtype=int)}))
            self.temp_max_dic.update(dict({city_name:np.asarray(save_temp_max_list,dtype=int)}))

            print("the" ,len(self.weather_dict.keys()),"city: ",city_name," result :" , np.asarray(save_weather_list,dtype=int).shape)

    def str2int_weather(self,weather_str):
        if "雪" in weather_str:
            return 2
        elif "雨" in weather_str:
            return 1
        else:
            return 0













if __name__ == '__main__':
    wdm = WeatherDataManager()