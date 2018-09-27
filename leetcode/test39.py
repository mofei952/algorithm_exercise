#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/9/27 17:54
# @File    : test39.py
# @Software: PyCharm

# Combination Sum
# 数字组合的和


class Solution(object):
    nums = []
    ret = []

    def dfs(self, candidates, target, index):
        if target < 0:
            return
        if target == 0:
            self.ret.append(self.nums[:])
        for i in range(index, len(candidates)):
            candidate = candidates[i]
            self.nums.append(candidate)
            self.dfs(candidates, target-candidate, i)
            self.nums.pop()

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.counts = []
        self.ret = []
        candidates.sort()
        self.dfs(candidates, target, 0)
        return self.ret


print(Solution().combinationSum([2,3,6,7],7))
