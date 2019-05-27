#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/5/25 10:33
# @File    : sort.py
# @Software: PyCharm

import random
import time
from copy import copy
from functools import wraps


def speed_test(func):
    @wraps(func)
    def inner(*args):
        t1 = time.perf_counter()
        result = func(*args)
        t2 = time.perf_counter()
        print(func.__doc__, t2 - t1)
        return result

    return inner


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

    def _merge_sort(arr, low, high):
        if high == low:
            return [arr[low]]
        mid = (low + high) // 2
        a = _merge_sort(arr, low, mid)
        b = _merge_sort(arr, mid + 1, high)
        return merge(a, b)

    return _merge_sort(arr, 0, len(arr) - 1)


def quick(arr, low, high):
    key = arr[low]
    while low < high:
        while low < high and arr[high] >= key:
            high -= 1
        arr[low] = arr[high]
        while low < high and arr[low] <= key:
            low += 1
        arr[high] = arr[low]
    arr[low] = key
    return low


@speed_test
def quick_sort(arr):
    """快速排序"""

    def _quick_sort(arr, low, high):
        if low < high:
            pos = quick(arr, low, high)
            _quick_sort(arr, low, pos - 1)
            _quick_sort(arr, pos + 1, high)
        return arr

    return _quick_sort(arr, 0, len(arr) - 1)


def heap_adjust(arr, i, length):
    left = 2 * i + 1
    right = 2 * i + 2
    min_index = i
    if left < length and arr[left] > arr[i]:
        min_index = left
    if right < length and arr[right] > arr[i] and arr[right] > arr[left]:
        min_index = right
    if min_index != i:
        arr[i], arr[min_index] = arr[min_index], arr[i]
        heap_adjust(arr, min_index, length)


@speed_test
def heap_sort(arr):
    """堆排序"""
    for i in range(len(arr) // 2 - 1, -1, -1):
        heap_adjust(arr, i, len(arr))
    for i in range(len(arr) - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heap_adjust(arr, 0, i)
    return arr


@speed_test
def counting_sort(arr):
    """计数排序"""
    max = arr[0]
    for v in arr:
        if v > max:
            max = v
    bucket = [0] * (max + 1)
    for v in arr:
        bucket[v] += 1
    i = 0
    for j in range(len(bucket)):
        count = bucket[j]
        while count:
            arr[i] = j
            i += 1
            count -= 1
    return arr


@speed_test
def bucket_sort(arr):
    pass


if __name__ == '__main__':
    count = 1000
    data = [random.randint(0, count * 10) for i in range(count)]

    result = sorted(data)
    assert bubble_sort(copy(data)) == result
    assert select_sort(copy(data)) == result
    assert insert_sort(copy(data)) == result
    assert shell_sort(copy(data)) == result
    assert merge_sort(copy(data)) == result
    assert quick_sort(copy(data)) == result
    assert heap_sort(copy(data)) == result
    # print(counting_sort(copy(data)))
    assert counting_sort(copy(data)) == result
