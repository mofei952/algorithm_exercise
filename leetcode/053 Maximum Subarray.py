#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/11/7 19:00
# @File    : 053 Maximum Subarray.py
# @Software: PyCharm

"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Follow up:
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""
from utils import print_time


class Solution:
    @print_time
    def maxSubArray(self, nums):
        """
        和最大的子列表
        :type nums: List[int]
        :rtype: int
        """
        sum = nums[0]
        max_sum = nums[0]
        for i in range(1, len(nums)):
            if sum < 0:
                sum = 0
            sum += nums[i]
            max_sum = max(sum, max_sum)
        return max_sum

    @print_time
    def maxSubArray2(self, nums):
        """
        和最大的子列表
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
        return max(nums)


if __name__ == '__main__':
    list = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    result = Solution().maxSubArray(list)
    print(result)
