#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/9/23 15:32
# @File    : t2fibonacci.py
# @Software: PyCharm


# 斐波那契数列
# https://www.nowcoder.com/practice/c6c7742f5ba7442aada113136ddea0c3?tpId=13&tqId=11160&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking


class Solution:
    def Fibonacci(self, n):
        if n < 2:
            return n
        a = 0
        b = 1
        for i in range(2, n + 1):
            a, b = b, a + b
        return b


for i in range(20):
    print(Solution().Fibonacci(i))
