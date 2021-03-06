#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/9/27 17:54
# @File    : 039 Combination Sum.py
# @Software: PyCharm

"""
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sums to target.
The same repeated number may be chosen from candidates unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]

Example 2:
Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        和为taget的数字组合
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        def dfs(target, index, nums):
            if target == 0:
                res.append(nums[:])
            for i in range(index, len(candidates)):
                candidate = candidates[i]
                if candidate > target:
                    break
                nums.append(candidate)
                dfs(target - candidate, i, nums)
                nums.pop()
        dfs(target, 0, [])
        return res


if __name__ == '__main__':
    result = Solution().combinationSum([2, 3, 6, 7], 7)
    print(result)
