#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/8/23 9:48
# @File    : test870.py
# @Software: PyCharm


class Solution(object):
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        a = sorted(A)
        b = sorted(B)
        a_index = 0
        dict = {}
        sheng_a_index_list = [i for i in range(len(a))]
        for b_index in range(len(b)):
            while a_index < len(a) and a[a_index] <= b[b_index]:
                a_index += 1
            if a_index < len(a):
                k = b[b_index]
                v = a[a_index]
                if k not in dict:
                    dict[k] = []
                dict[k].append(v)
                sheng_a_index_list.remove(a_index)
                a_index += 1
            else:
                break

        for i in range(b_index, len(b)):
            if len(sheng_a_index_list) == 0:
                break
            k = b[i]
            v = a[sheng_a_index_list[0]]
            sheng_a_index_list.pop(0)
            if k not in dict:
                dict[k] = []
            dict[k].append(v)

        aa = []
        for i in B:
            aa.append(dict[i][0])
            dict[i].pop(0)

        return aa


a = Solution().advantageCount([2, 0, 4, 1, 2], [1, 3, 0, 0, 2])
print (a)
