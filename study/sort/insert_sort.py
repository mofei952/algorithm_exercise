#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/5/29 20:14
# @File    : insert_sort.py
# @Software: PyCharm

import random
from copy import copy

from study.util import running_time


@running_time
def insert_sort(arr):
    """插入排序"""
    for i in range(1, len(arr)):
        j = i - 1
        while j >= 0 and arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            j -= 1
    return arr


@running_time
def insert_sort1(arr):
    """插入排序优化"""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def binary_search(arr, low, high, key):
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > key:
            high = mid - 1
        else:
            low = mid + 1
    return low


@running_time
def binary_insert_sort(arr):
    """插入排序优化（二分插入排序）"""
    for i in range(1, len(arr)):
        key = arr[i]
        pos = binary_search(arr, 0, i - 1, key)
        for j in range(i - 1, pos - 1, -1):
            arr[j + 1] = arr[j]
        arr[pos] = key
    return arr


if __name__ == '__main__':
    count = 10000
    data = [random.randint(-count, count) for i in range(count)]

    sorted_data = sorted(data)
    assert insert_sort(copy(data)) == sorted_data
    assert insert_sort1(copy(data)) == sorted_data
    assert binary_insert_sort(copy(data)) == sorted_data
