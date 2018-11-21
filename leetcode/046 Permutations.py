#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/11/7 18:11
# @File    : 046 Permutations.py
# @Software: PyCharm

"""
Given a collection of distinct integers, return all possible permutations.

Example:
Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""


class Solution:
    def permute(self, nums):
        """
        返回所有可能的排列
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        if len(nums) == 1:
            return [nums]
        result = []
        for i in nums:
            t = nums[:]
            t.remove(i)
            list = self.permute(t)
            for item in list:
                item.insert(0, i)
            result.extend(list)
        return result


if __name__ == '__main__':
    result = Solution().permute([1, 2, 3, 4, 6])
    print(result)
