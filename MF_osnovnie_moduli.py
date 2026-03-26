#основнше модули
#os sis папки файлы
import os, sys
print(os.listdir())

import math #математический и статистический модули
from math import sin, cos, pi, exp
from statistics import mean

import glob #отбирает файлы по заданым параметрам
print(glob.glob('*_*.py'))

#временной модуль
import time
print(time.time())
def timer():  # проверили время сна функции
    time.sleep(1)
start = time.time()
timer()
print(time.time() - start)

#datetime
import datetime
print(datetime.datetime.now())