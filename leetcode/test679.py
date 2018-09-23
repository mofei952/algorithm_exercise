#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/8/23 15:55
# @File    : test679.py
# @Software: PyCharm
import copy


class Solution(object):
    def game(self, nums):
        if len(nums) == 1:
            return abs(nums[0] - 24) <= 1 * 10 ** -5
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                a = nums[i]
                b = nums[j]
                tmp_nums = copy.copy(nums)
                tmp_nums.remove(a)
                tmp_nums.remove(b)
                list = [a + b, a - b, b - a, a * b]
                if b != 0:
                    list.append(float(a) / b)
                if a != 0:
                    list.append(float(b) / a)
                list = set(list)
                for k in list:
                    t_nums = copy.copy(tmp_nums)
                    t_nums.append(k)
                    r = self.game(t_nums)
                    if r:
                        return True
                    # if len(nums) == 3:
                    # print nums, tmp_nums, k, r

        return False

    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return self.game(nums)


a = Solution().judgePoint24([1, 2, 1, 2])
print (a)
