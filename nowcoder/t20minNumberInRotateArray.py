#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/10/9 19:45
# @File    : t20minNumberInRotateArray.py
# @Software: PyCharm


# 旋转数组的最小数字
# https://www.nowcoder.com/practice/9f3231a991af4f55b95579b44b7a01ba?tpId=13&tqId=11159&tPage=2&rp=2&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking

class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if not rotateArray:
            return 0
        min = 0
        max = len(rotateArray) - 1
        while min <= max:
            mid = (min + max) // 2
            if rotateArray[mid] < rotateArray[mid - 1]:
                return rotateArray[mid]
            if rotateArray[mid] > rotateArray[max]:
                min = mid + 1
            else:
                max = mid - 1
        return rotateArray[mid]


print(Solution().minNumberInRotateArray([3, 4, 5, 6, 1]))
