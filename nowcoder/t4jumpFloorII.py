#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/9/23 15:43
# @File    : t4jumpFloorII.py
# @Software: PyCharm

# 变态跳台阶
# https://www.nowcoder.com/practice/22243d016f6b47f2a6928b4313c85387?tpId=13&tqId=11162&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking

class Solution:
    def jumpFloorII(self, number):
        return 2 ** (number - 1)


print(Solution().jumpFloorII(4))
