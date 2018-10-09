#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/10/9 19:26
# @File    : t18maxInWindows.py
# @Software: PyCharm

# 滑动窗口的最大值
# https://www.nowcoder.com/practice/1624bc35a45c42c0bc17d17fa0cba788?tpId=13&tqId=11217&tPage=2&rp=2&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking


class Solution:
    def maxInWindows(self, num, size):
        if size == 0:
            return []
        stack = []
        result = []
        for i in range(len(num)):
            while stack and stack[-1][0] < num[i]:
                stack.pop()
            stack.append((num[i], i))
            if i >= size-1:
                while stack and stack[0][1] <= i - size:
                    stack.pop(0)
                result.append(stack[0][0])
        return result


print(Solution().maxInWindows([10,14,12,11],0))
