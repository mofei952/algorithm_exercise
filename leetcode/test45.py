#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/9/17 20:34
# @File    : test.py
# @Software: PyCharm

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        begin = 0
        end = 1
        step = 0
        while end < len(nums):
            next = -1
            for i in range(begin, end):
                next = max(next, nums[i] + i)
            begin = end
            end = next+1
            step += 1
        return step
a = Solution().jump([1 for i in range(1000)])
print(a)
