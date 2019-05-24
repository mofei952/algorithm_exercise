#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/4/30 14:09
# @File    : sort.py
# @Software: PyCharm

import random
from collections import defaultdict
from copy import copy

import time
from functools import wraps

from study.tree.bst import BinarySearchTree
from study.tree.tree_node import TreeNode


def speed_test(times=1):
    def wrapper(func):
        @wraps(func)
        def inner(*args):
            t1 = time.perf_counter()
            result = None
            for i in range(times):
                result = func(*args)
            t2 = time.perf_counter()
            return t2 - t1, result

        return inner

    return wrapper


@speed_test()
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


@speed_test()
def insert_sort_reversed(arr):
    """插入排序(从大到小)"""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def bin_search(arr, low, high, key):
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return low


@speed_test()
def bin_insert_sort(arr):
    """二分插入排序"""
    for i in range(1, len(arr)):
        key = arr[i]
        pos = bin_search(arr, 0, i - 1, key)
        for j in range(i - 1, pos - 1, -1):
            arr[j + 1] = arr[j]
        arr[pos] = key
    return arr


def create_bin_search_tree(arr):
    if not arr:
        return None
    TreeNode(arr[0])


@speed_test()
def bin_search_tree_sort(arr):
    """利用二叉搜索树进行排序"""
    bst = BinarySearchTree()
    for i in arr:
        bst.insert(i)
    return bst.inorderTraversal()


if __name__ == '__main__':
    count = 1000
    times = 1

    test_data = [
        [random.randint(0, count) for i in range(count)],
        [i for i in range(count)],
        [count - i for i in range(count)]
    ]

    t_dict = defaultdict(list)
    for data in test_data:
        for fun in [insert_sort, insert_sort_reversed, bin_insert_sort, bin_search_tree_sort]:
            t, res = fun(copy(data))
            t_dict[fun.__name__].append(t)

    f_list = ['随机数列表', '升序列表', '降序列表']
    for name, t_list in t_dict.items():
        print(name)
        res_list = list(zip(f_list, t_list))
        for f, t in res_list:
            print(f, '\t', t)
        print('总', '\t\t\t', sum(t_list))
        print()
