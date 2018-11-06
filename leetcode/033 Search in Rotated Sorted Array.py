#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/11/6 12:53
# @File    : 033 Search in Rotated Sorted Array.py
# @Software: PyCharm

"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.
Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""


class Solution:
    def search(self, nums, target):
        """
        在升序排列并移动位置的列表中查找target
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                if nums[low] > nums[mid] or nums[low] <= target:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] > nums[high] or nums[high] >= target:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1


if __name__ == '__main__':
    list = [4, 5, 6, 7, 0, 1, 2]
    list2 = [4, 5, 6, 7, 0, 1, 2, 8, 3]
    for i in list2:
        result = Solution().search(list, i)
        print(result)
