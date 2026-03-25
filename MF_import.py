#import
import os
os.getcwd()
print(os.getcwd())
print(os.path.join(os.getcwd(), '..'))

#импорт элементов из модуля
from os import getcwd
print(getcwd())

from math import sin, cos, pi
print(sin(1))
print(cos(1))

from math import * #импортирует все модули

#алиасы
import pandas as pd
import numpy as np  # так обзывают коротко библиотеки