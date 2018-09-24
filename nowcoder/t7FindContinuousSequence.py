#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/9/24 17:49
# @File    : t7FindContinuousSequence.py
# @Software: PyCharm

#和为S的连续正数序列
#https://www.nowcoder.com/practice/c451a3fd84b64cb19485dad758a55ebe?tpId=13&tqId=11194&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking

class Solution:
    def FindContinuousSequence(self, tsum):
        ret = []
        for i in range(1, tsum):
            for j in range(i+1, tsum):
                s = (i + j) * (j - i + 1) / 2
                if s == tsum:
                    ret.append(list(range(i,j+1)))
                elif s > tsum:
                    break
        return ret
print(Solution().FindContinuousSequence(100))

