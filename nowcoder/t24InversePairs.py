#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/10/25 21:23
# @File    : t24InversePairs.py
# @Software: PyCharm

import bisect


# 数组中的逆序对
# https://www.nowcoder.com/practice/96bd6684e04a44eb80e6a68efc0ec6c5?tpId=13&tqId=11188&tPage=2&rp=2&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking

class Solution:
    count = 0

    def InversePairs(self, data):
        data.reverse()
        data_sorted = []
        count = 0
        for d in data:
            index = bisect.bisect_left(data_sorted, d)
            data_sorted.insert(index, d)
            count += index
        return count % 1000000007

    def InversePairs2(self, data):
        self.count = 0
        self.merge_sort(data, 0, len(data) - 1)
        return self.count

    def merge_sort(self, data, left, right):
        if left < right:
            mid = (left + right) // 2
            self.merge_sort(data, left, mid)
            self.merge_sort(data, mid + 1, right)
            self.merge(data, left, mid, right)

    def merge(self, data, left, mid, right):
        temp = []
        l = mid
        r = right
        while l >= left and r >= mid + 1:
            if data[l] > data[r]:
                self.count += (r - mid) % 1000000007
                temp.insert(0, data[l])
                l -= 1
            elif data[l] < data[r]:
                temp.insert(0, data[r])
                r -= 1
        while l >= left:
            temp.insert(0, data[l])
            l -= 1
        while r >= mid + 1:
            temp.insert(0, data[r])
            r -= 1
        data[left:right + 1] = temp


print(Solution().InversePairs2([364, 637, 341, 406, 747, 995, 234, 971, 571, 219, 993, 407,
                                416, 366, 315, 301, 601, 650, 418, 355, 460, 505, 360, 965,
                                516, 648, 727, 667, 465, 849, 455, 181, 486, 149, 588, 233,
                                144, 174, 557, 67, 746, 550, 474, 162, 268, 142, 463, 221, 882,
                                576, 604, 739, 288, 569, 256, 936, 275, 401, 497, 82, 935, 983,
                                583, 523, 697, 478, 147, 795, 380, 973, 958, 115, 773, 870,
                                259, 655, 446, 863, 735, 784, 3, 671, 433, 630, 425, 930, 64,
                                266, 235, 187, 284, 665, 874, 80, 45, 848, 38, 811, 267, 575]))
