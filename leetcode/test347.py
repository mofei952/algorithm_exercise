#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/9/27 17:15
# @File    : test347.py
# @Software: PyCharm

# Top K Frequent Elements
# 最频繁出现的k个元素

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        num_count = {}
        count_numlist = {}
        max_count = 0
        for i in nums:
            if i not in num_count:
                num_count[i] = 1
            else:
                num_count[i] += 1
            if num_count[i] > max_count:
                max_count = num_count[i]
        for num, count in num_count.items():
            if count not in count_numlist:
                count_numlist[count] = [num]
            else:
                count_numlist[count].append(num)
        ret = []
        for i in range(max_count, 0, -1):
            if i not in count_numlist:
                continue
            numlist = count_numlist[i]
            for j in numlist:
                ret.append(j)
            if len(ret) == k:
                break
        return ret[:k]

print(Solution().topKFrequent([5,3,1,1,1,3,73,1],2))