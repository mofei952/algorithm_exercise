#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/5/29 16:36
# @File    : select_sort.py
# @Software: PyCharm

import random
from copy import copy

from study.util import running_time


@running_time
def select_sort(arr):
    """选择排序"""
    for i in range(len(arr) - 1):
        min = arr[i]
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < min:
                min = arr[j]
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


@running_time
def select_sort1(arr):
    """选择排序优化"""
    low = 0
    high = len(arr) - 1
    while low < high:
        min = max = low
        for i in range(low, high + 1):
            if arr[i] < arr[min]:
                min = i
            if arr[i] > arr[max]:
                max = i
        if arr[min] != arr[low]:
            arr[low], arr[min] = arr[min], arr[low]
        if max == low:
            max = min
        if arr[max] != arr[high]:
            arr[high], arr[max] = arr[max], arr[high]
        low += 1
        high -= 1
    return arr


if __name__ == '__main__':
    count = 10
    data = [random.randint(-count, count) for i in range(count)]

    sorted_data = sorted(data)
    assert select_sort(copy(data)) == sorted_data
    assert select_sort1(copy(data)) == sorted_data
