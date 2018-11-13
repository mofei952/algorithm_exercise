#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/11/12 21:02
# @File    : 023 Merge k Sorted Lists.py
# @Software: PyCharm

"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""


class Solution:
    def nextPermutation(self, nums):
        """
        比nums大的下一种排列
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                # nums[i:]中 比nums[i-1]大的并且最接近nums[i-1], 和nums[i-1]交换位置
                cloest_index = i
                for j in range(i, len(nums)):
                    if nums[j] > nums[i - 1]:
                        cloest_index = j
                nums[cloest_index], nums[i - 1] = nums[i - 1], nums[cloest_index]
                # nums[i:]进行排序
                nums[i:] = sorted(nums[i:])
                break
        else:
            nums.reverse()


if __name__ == '__main__':
    nums = [6, 5, 5, 7, 2]
    Solution().nextPermutation(nums)
    print(nums)
