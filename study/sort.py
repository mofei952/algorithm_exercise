#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/5/25 10:33
# @File    : sort.py
# @Software: PyCharm

import random
from copy import copy

from study.utils import speed_test


@speed_test
def bubble_sort(arr):
    """冒泡排序"""
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


@speed_test
def select_sort(arr):
    """选择排序"""
    for i in range(len(arr) - 1):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


@speed_test
def insert_sort(arr):
    """插入排序"""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


@speed_test
def shell_sort(arr):
    """希尔排序"""
    gap = len(arr) // 2
    while gap:
        for i in range(gap, len(arr)):
            key = arr[i]
            j = i - gap
            while j >= 0 and arr[j] > key:
                arr[j + gap] = arr[j]
                j -= gap
            arr[j + gap] = key
        gap //= 2
    return arr


def merge(arr1, arr2):
    i = j = 0
    arr3 = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            arr3.append(arr1[i])
            i += 1
        else:
            arr3.append(arr2[j])
            j += 1
    if i < len(arr1):
        for k in range(i, len(arr1)):
            arr3.append(arr1[k])
    elif j < len(arr2):
        for k in range(j, len(arr2)):
            arr3.append(arr2[k])
    return arr3


@speed_test
def merge_sort(arr):
    """归并排序"""

    def _merge_sort(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        a = _merge_sort(arr[:mid])
        b = _merge_sort(arr[mid:])
        return merge(a, b)

    return _merge_sort(arr)


if __name__ == '__main__':
    count = 1000
    data = [random.randint(0, count * 10) for i in range(count)]

    result = sorted(data)
    assert bubble_sort(copy(data)) == result
    assert select_sort(copy(data)) == result
    assert insert_sort(copy(data)) == result
    assert shell_sort(copy(data)) == result
    assert merge_sort(copy(data)) == result
