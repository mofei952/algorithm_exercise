#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/9/24 17:54
# @File    : t8LeftRotateString.py
# @Software: PyCharm

# 左旋转字符串
# https://www.nowcoder.com/practice/12d959b108cb42b1ab72cef4d36af5ec?tpId=13&tqId=11196&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking

class Solution:
    def LeftRotateString(self, s, n):
        if not s:
            return ''
        n = n % len(s)
        return s[n:] + s[:n]


print(Solution().LeftRotateString('zxcvaaa', 10))
