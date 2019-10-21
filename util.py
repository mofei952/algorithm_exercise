#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/5/28 21:21
# @File    : util.py
# @Software: PyCharm

import time

from functools import wraps


def running_time(func):
    """运行时间装饰器"""

    @wraps(func)
    def wrapper(*args, print_time=True):
        t1 = time.perf_counter()
        result = func(*args)
        t2 = time.perf_counter()
        if print_time:
            print(func.__name__, t2 - t1, sep='\t')
        return result

    return wrapper
