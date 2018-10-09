#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/10/9 19:51
# @File    : t21GetUglyNumber.py
# @Software: PyCharm

#丑数
#https://www.nowcoder.com/practice/6aa9e04fc3794f68acf8778237ba065b?tpId=13&tqId=11186&tPage=2&rp=2&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking
from heapq import heappush, heappop


class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index < 1:
            return 0
        heap = []
        val = 1
        idx = 1
        last_val = None
        heappush(heap, val)
        while idx <= index:
            val = heappop(heap)
            while val == last_val:
                val = heappop(heap)
            last_val = val
            heappush(heap, val * 2)
            heappush(heap, val * 3)
            heappush(heap, val * 5)
            idx += 1
        return val

print(Solution().GetUglyNumber_Solution(1))