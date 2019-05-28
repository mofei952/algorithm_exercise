#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/5/25 10:33
# @File    : sort.py
# @Software: PyCharm

import random
from copy import copy

from study.util import running_time


@running_time
def bubble_sort(arr):
    """冒泡排序"""
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


@running_time
def select_sort(arr):
    """选择排序"""
    for i in range(len(arr) - 1):
        min = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    return arr


@running_time
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


@running_time
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
    arr3 = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            arr3.append(arr1[i])
            i += 1
        else:
            arr3.append(arr2[j])
            j += 1
    for k in range(i, len(arr1)):
        arr3.append(arr1[k])
    for k in range(j, len(arr2)):
        arr3.append(arr2[k])
    return arr3


@running_time
def merge_sort(arr):
    """归并排序"""

    def _merge_sort(arr, low, high):
        if low == high:
            return [arr[low]]
        mid = (low + high) // 2
        arr1 = _merge_sort(arr, low, mid)
        arr2 = _merge_sort(arr, mid + 1, high)
        return merge(arr1, arr2)

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


@running_time
def quick_sort(arr):
    """快速排序"""

    def _quick_sort(arr, low, high):
        if low >= high:
            return
        pos = quick(arr, low, high)
        _quick_sort(arr, low, pos - 1)
        _quick_sort(arr, pos + 1, high)

    _quick_sort(arr, 0, len(arr) - 1)
    return arr


def heap_adjust(arr, i, length):
    left = 2 * i + 1
    right = 2 * i + 2
    min = i
    if left < length and arr[left] > arr[min]:
        min = left
    if right < length and arr[right] > arr[min]:
        min = right
    if min != i:
        arr[i], arr[min] = arr[min], arr[i]
        heap_adjust(arr, min, length)


@running_time
def heap_sort(arr):
    """堆排序"""
    for i in range(len(arr) // 2 - 1, -1, -1):
        heap_adjust(arr, i, len(arr))
    for i in range(len(arr) - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heap_adjust(arr, 0, i)
    return arr


@running_time
def count_sort(arr):
    """计数排序"""
    min = max = arr[0]
    for v in arr:
        if v > max:
            max = v
        if v < min:
            min = v
    count_list = [0] * (max - min + 1)
    for v in arr:
        count_list[v - min] += 1
    i = 0
    for j in range(len(count_list)):
        count = count_list[j]
        for k in range(count):
            arr[i] = j + min
            i += 1
    return arr


@running_time
def bucket_sort(arr):
    """桶排序"""
    min = max = arr[0]
    for v in arr:
        if v < min:
            min = v
        if v > max:
            max = v
    bucket_size = 10
    bucket_count = (max - min) // bucket_size + 1
    buckets = [[] for i in range(bucket_count)]
    for v in arr:
        index = (v - min) // bucket_size
        buckets[index].append(v)
    i = 0
    for bucket in buckets:
        insert_sort(bucket, print_time=False)
        for v in bucket:
            arr[i] = v
            i += 1
    return arr


def radix(arr):
    max = arr[0]
    for v in arr:
        if v > max:
            max = v
    num = 1
    while num <= max:
        digit_list = [[] for i in range(10)]
        for v in arr:
            index = v // num % 10
            digit_list[index].append(v)
        i = 0
        for values in digit_list:
            for v in values:
                arr[i] = v
                i += 1
        num *= 10
    return arr


@running_time
def radix_sort(arr):
    """基数排序"""
    positive_arr = []
    negative_arr = []
    for v in arr:
        if v >= 0:
            positive_arr.append(v)
        else:
            negative_arr.append(-v)
    radix(positive_arr)
    radix(negative_arr)
    sorted_arr = [-v for v in negative_arr[::-1]] + positive_arr
    return sorted_arr


if __name__ == '__main__':
    count = 1000
    data = [random.randint(-count, count) for i in range(count)]

    sort_data = sorted(data)
    assert bubble_sort(copy(data)) == sort_data
    assert select_sort(copy(data)) == sort_data
    assert insert_sort(copy(data)) == sort_data
    assert shell_sort(copy(data)) == sort_data
    assert merge_sort(copy(data)) == sort_data
    assert quick_sort(copy(data)) == sort_data
    assert heap_sort(copy(data)) == sort_data
    assert count_sort(copy(data)) == sort_data
    assert bucket_sort(copy(data)) == sort_data
    assert radix_sort(copy(data)) == sort_data
