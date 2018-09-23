#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/6/29 9:32
# @File    : t514.py
# @Software: PyCharm

class Solution:
    """
    @param n: non-negative integer, n posts
    @param k: non-negative integer, k colors
    @return: an integer, the total number of ways
    """

    def numWays(self, n, k):
        # write your code here
        if k == 1:
            return 1 if n < 3 else 0
        s = 0
        for i in range(0, n / 2 + 1):
            s += self.c(n - i, i)*k*(k-1)**(n-i-1)
        return s

    def c(self, n, m):
        if m > n / 2:
            m = n - m

        s1 = 1
        s2 = 1
        for i in range(n - m + 1, n + 1):
            s1 *= i
        for i in range(1, m + 1):
            s2 *= i
        return s1 / s2


print (Solution().numWays(1314520, 1))
