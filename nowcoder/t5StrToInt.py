#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/9/24 17:15
# @File    : t5StrToInt.py
# @Software: PyCharm


# 把字符串转换成整数
# https://www.nowcoder.com/practice/1277c681251b4372bdef344468e4f26e?tpId=13&tqId=11202&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking

class Solution:
    def StrToInt(self, s):
        if not s:
            return 0
        sign = 1
        index = 0
        sum = 0
        if s[0] == '-':
            sign = -1
            index = 1
        if s[0] == '+':
            index = 1
        for i in s[index:]:
            if i < '0' or i > '9':
                return 0
            sum = sum * 10 + int(i)
        return sign * sum


print(Solution().StrToInt('+15644'))
