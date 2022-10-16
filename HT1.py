#!/usr/bin/env python
# coding: utf-8

# In[65]:


import random
import numpy as np
import time
from statistics import mean

data_list = np.random.randint(0, 1000, size=1000000)  #Заполнение массива

def calcHist(data_list):                       #Поиск и заполнение массива с диапазонами
    
    hist= [0] * 10

    for i in array:                       
        if ( 0<data_list[i]<100):
            hist[0]+=1
        elif ( 100<data_list[i]<200):
            hist[1]+=1
        elif ( 200<data_list[i]<300):
            hist[2]+=1
        elif ( 300<data_list[i]<400):
            hist[3]+=1
        elif ( 400<data_list[i]<500):
            hist[4]+=1
        elif ( 500<data_list[i]<600):
            hist[5]+=1
        elif ( 600<data_list[i]<700):
            hist[6]+=1
        elif ( 700<data_list[i]<800):
            hist[7]+=1
        elif ( 800<data_list[i]<900):
            hist[8]+=1
        else:
            hist[9]+=1
    return hist

count_array=calcHist(data_list)
print(count_array)
                 
check = 0    
for i in range (0, 10):                  #Проверка количества значений
    check += count_array[i]
print(check)

#Определение Времени
time_array = [0] * 10

for i in range(0,10):                   #Пока не работает
    start_time = time.time()            
    calcHist(data_list)
    end_time = time.time()
    time_array[i]= end_time-start_time

max_time=max(time_array)
min_time=min(time_array)
average_time= mean(time_array)

print(max_time,min_time,average_time)


# In[ ]:




