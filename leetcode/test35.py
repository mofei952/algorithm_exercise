#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/9/27 17:46
# @File    : test35.py
# @Software: PyCharm


# Search Insert Position
# 查找插入位置


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i] == target or nums[i] > target:
                return i
        return len(nums)


print(Solution().searchInsert([1,3,5,6], 2))