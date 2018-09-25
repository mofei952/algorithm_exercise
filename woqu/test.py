#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/9/25 23:09
# @File    : test.py
# @Software: PyCharm

# list反转的方法
# 1
a = [3, 1, 4]
a.reverse()
print(a)
# 2
a = list(reversed(a))
print(a)
# 3
a = a[::-1]
print(a)
# 4
for i in range(len(a) // 2):
    a[i], a[len(a) - i - 1] = a[len(a) - i - 1], a[i]
print(a)
