#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/9/23 15:36
# @File    : t3jumpFloor.py
# @Software: PyCharm

# 跳台阶
# https://www.nowcoder.com/practice/8c82a5b80378478f9484d87d1c5f12a4?tpId=13&tqId=11161&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking

class Solution:
    def jumpFloor(self, number):
        if number <= 2:
            return number
        a = 1
        b = 2
        for i in range(3, number + 1):
            a, b = b, a + b
        return b


print(Solution().jumpFloor(3))
