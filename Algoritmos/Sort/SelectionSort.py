import numpy as np
import random
import timeit


def selection_sort(array):
    n = len(array)

    for i in range(n):
        id_min = i
        for j in range(i +1, n):
            if array[id_min] > array[j]:
                id_min = j
        temp = array[i]
        array[i] = array[id_min]
        array[id_min] = temp
    
    return array
