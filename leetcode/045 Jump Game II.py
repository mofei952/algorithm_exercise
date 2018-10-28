#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/9/17 20:34
# @File    : 045 Jump Game II.py
# @Software: PyCharm


"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Your goal is to reach the last index in the minimum number of jumps.

Example:
Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.

Note:
You can assume that you can always reach the last index.
"""


class Solution(object):
    def jump(self, nums):
        """
        跳跃的步数
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
            end = next + 1
            step += 1
        return step


if __name__ == '__main__':
    res = Solution().jump([1 for i in range(1000)])
    print(res)
