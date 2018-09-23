#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/8/24 16:37
# @File    : test368.py
# @Software: PyCharm
import copy


class number():
    def __init__(self, n):
        self.n = n
        self.number_list = []

    def quyu(self, num):
        return self.n % num.n == 0


class Solution(object):
    longest_num_list = []
    max_length = 0

    def dfs(self, node, num):
        if num.quyu(node):
            if not node.number_list:
                node.number_list.append(copy.deepcopy(num))
                return True
            flag = False
            for num1 in node.number_list:
                if self.dfs(num1, num):
                    flag = True
            if not flag:
                node.number_list.append(copy.deepcopy(num))
            return True
        else:
            return False

    def print_tree(self, root):
        a = [[root, 0]]
        while a:
            r, l = a.pop(0)
            for i in r.number_list:
                print ('-' * l + str(i.n))
                a.append([i, l + 1])

    def dfs2(self, node, num_list):
        num_list.append(node.n)
        if not node.number_list:
            length = len(num_list)
            if length > self.max_length:
                self.max_length = length
                self.longest_num_list = copy.copy(num_list)
        else:
            for n in node.number_list:
                self.dfs2(n, num_list)
        num_list.remove(node.n)

    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []

        nums.sort()

        dp = []
        max_count = -1
        max_index = -1
        for i in range(len(nums)):
            dp.append(1)
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[i], dp[j] + 1)
            if dp[i] > max_count:
                max_count = dp[i]
                max_index = i
        # print max_count, max_index

        index = max_index
        result_list = []
        while index >= 0:
            if dp[index] == max_count:
                if not result_list or result_list[-1] % nums[index] == 0:
                    result_list.append(nums[index])
                    max_count -= 1
            index -= 1
        result_list.reverse()
        return result_list

        # nums.sort()
        # root = number(1)
        # for i in nums:
        #     num = number(i)
        #     self.dfs(root, num)
        #
        # # self.print_tree(root)
        # self.dfs2(root, [])
        # return self.longest_num_list[1:]



        # if not nums:
        #     return []
        #
        # nums.sort(reverse=True)
        #
        # result_list = []
        # result_list.append([nums[0]])
        # max_count = len(result_list[0])
        # result = result_list[0]
        #
        # for i in range(1, len(nums)):
        #     n = nums[i]
        #     enable = False
        #     j = 0
        #     while j < len(result_list):
        #         r = result_list[j]
        #         enable = False
        #         if r[-1] % n == 0:
        #             enable = True
        #             result_list.insert(j + 1, copy.copy(result_list[j]))
        #             result_list[j].append(n)
        #             if len(result_list[j]) > max_count:
        #                 result = result_list[j]
        #                 max_count = len(result_list[j])
        #             j += 1
        #         j += 1
        #     if not enable:
        #         result_list.append([n])
        #
        # return result


a = Solution().largestDivisibleSubset([1,2,3])
print (a)
