#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/5/28 19:18
# @File    : bubble_sort.py
# @Software: PyCharm

import random
from copy import copy

from study.sort.sort import running_time


@running_time
def bubble_sort(arr):
    """冒泡排序"""
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


@running_time
def bubble_sort1(arr):
    """冒泡排序优化1"""
    for i in range(len(arr) - 1):
        flag = 0
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = 1
        if not flag:
            break
    return arr


@running_time
def bubble_sort2(arr):
    """冒泡排序优化2"""
    i = len(arr) - 1
    while i:
        pos = 0
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                pos = j
        i = pos
    return arr


@running_time
def cocktail_sort(arr):
    """鸡尾酒排序"""
    low = 0
    high = len(arr) - 1
    while low < high:
        for i in range(low, high):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        high -= 1
        for i in range(high, low, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
        low += 1
    return arr


@running_time
def cocktail_sort1(arr):
    """鸡尾酒排序优化1"""
    low = 0
    high = len(arr) - 1
    while low < high:
        for i in range(low, high):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        high -= 1
        flag = 0
        for i in range(high, low, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                flag = 1
        low += 1
        if not flag:
            break
    return arr


@running_time
def cocktail_sort2(arr):
    """鸡尾酒排序优化2"""
    low = 0
    high = len(arr) - 1
    while low < high:
        pos = low
        for i in range(low, high):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                pos = i
        high = pos
        pos = high
        for i in range(high, low, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                pos = i
        low = pos
    return arr


if __name__ == '__main__':
    count = 1000
    # 对于随机序列，鸡尾酒排序优化12稍快一点
    # data = [random.randint(-count, count) for i in range(count)]
    # 对于已经有序的序列，冒泡排序优化1的效率比一般冒泡快，鸡尾酒排序优化1比鸡尾酒排序快
    # data = [i for i in range(count)]
    # 对于后面大部分有序的序列，优化2的效率比优化1高
    # data = [1 if i == 30 else i for i in range(count)]
    # 对于前面大部分有序的序列，鸡尾酒排序优化12比其他几种都快
    data = [i for i in range(count)] + [1]

    sort_data = sorted(data)
    assert bubble_sort(copy(data)) == sort_data
    assert bubble_sort1(copy(data)) == sort_data
    assert bubble_sort2(copy(data)) == sort_data
    assert cocktail_sort(copy(data)) == sort_data
    assert cocktail_sort1(copy(data)) == sort_data
    assert cocktail_sort2(copy(data)) == sort_data
