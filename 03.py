import numpy as np

from math import factorial

arr=  np.array([100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150])


def mean_value(array):
    return sum(array)/len(array)

print(f'Среднее арифметическое для данной выборки М(Х) = {mean_value(arr): .2f}')

