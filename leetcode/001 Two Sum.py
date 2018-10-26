#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/10/26 19:54
# @File    : 001 Two Sum.py
# @Software: PyCharm

"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for index, num in enumerate(nums):
            if target - num in dict:
                return dict[target - num], index
            dict[num] = index


if __name__ == '__main__':
    result = Solution().twoSum([2, 7, 11, 15], 9)
    print(result)
