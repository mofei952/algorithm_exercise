#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/11/7 17:55
# @File    : 034 Find First and Last Position of Element in Sorted Array.py
# @Software: PyCharm

"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
Your algorithm's runtime complexity must be in the order of O(log n).
If the target is not found in the array, return [-1, -1].

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""


class Solution:
    def searchRange(self, nums, target):
        """
        查找目标值的起始范围
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = [-1, -1]

        def find(max):
            low = 0
            high = len(nums) - 1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    if max:
                        if mid == 0 or nums[mid - 1] < target:
                            result[0] = mid
                            break
                        else:
                            high = mid - 1
                    else:
                        if mid == len(nums) - 1 or nums[mid + 1] > target:
                            result[1] = mid
                            break
                        else:
                            low = mid + 1
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1

        find(0)
        find(1)
        return result


if __name__ == '__main__':
    result = Solution().searchRange([5, 7, 7, 8, 8, 10], 7)
    print(result)
