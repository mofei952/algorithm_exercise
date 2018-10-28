#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/9/27 17:46
# @File    : 035 Search Insert Position.py
# @Software: PyCharm

"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.

Example 1:
Input: [1,3,5,6], 5
Output: 2

Example 2:
Input: [1,3,5,6], 2
Output: 1

Example 3:
Input: [1,3,5,6], 7
Output: 4

Example 4:
Input: [1,3,5,6], 0
Output: 0
"""


class Solution(object):
    def searchInsert(self, nums, target):
        """
        查找插入位置
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i] == target or nums[i] > target:
                return i
        return len(nums)

    def searchInsert2(self, nums, target):
        """
        查找插入位置，使用二分查找
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target or nums[mid] > target > nums[mid - 1]:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return low


if __name__ == '__main__':
    result = Solution().searchInsert2([1, 3, 5, 6], 7)
    print(result)
