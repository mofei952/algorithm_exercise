#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/9/24 17:57
# @File    : t9GetNumberOfK.py
# @Software: PyCharm

# 数字在排序数组中出现的次数
# https://www.nowcoder.com/practice/70610bf967994b22bb1c26f9ae901fa2?tpId=13&tqId=11190&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking


class Solution:
    def GetNumberOfK(self, data, k):
        start = 0
        end = len(data) - 1
        count = 0
        while start <= end:
            mid = (end + start) // 2
            if data[mid] == k:
                t = mid
                while t >= 0 and data[t] == k:
                    t -= 1
                    count += 1
                t = mid + 1
                while t < len(data) and data[t] == k:
                    t += 1
                    count += 1
                return count
            elif data[mid] < k:
                start = mid + 1
            else:
                end = mid - 1
        return 0


print(Solution().GetNumberOfK([3], 3))
