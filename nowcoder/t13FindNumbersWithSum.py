#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/9/24 23:10
# @File    : t13FindNumbersWithSum.py
# @Software: PyCharm

# 和为S的两个数字
# https://www.nowcoder.com/practice/390da4f7a00f44bea7c2f3d19491311b?tpId=13&tqId=11195&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking

class Solution:
    def FindNumbersWithSum(self, array, tsum):
        for i in array:
            if tsum - i in array:
                return [i, tsum - i]
        return []


print(Solution().FindNumbersWithSum([1, 2, 4, 7, 11, 16], 10))
