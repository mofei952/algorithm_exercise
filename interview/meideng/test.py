#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/9/27 10:23
# @File    : test.py
# @Software: PyCharm


a = [1, 2, 2, 4]
b = [1, 2, 3]

indexb = len(b) - 1
indexa = len(a) - 1
while indexa >= 0 and indexb >= 0:
    if a[indexa] == b[indexb]:
        a.pop(indexa)
        indexa -= 1
    elif a[indexa] < b[indexb]:
        indexb -= 1
    else:
        indexa -= 1
print(a)
