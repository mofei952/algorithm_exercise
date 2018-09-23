#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/8/22 17:33
# @File    : test816.py
# @Software: PyCharm
import re


class Solution(object):
    def fuhe(self, s):
        return re.match('^(([^0]\d*)|0)(\.\d*[^0])?$', s) is not None

    def num_list_after_add_dian(self, s):
        if len(s) == 1:
            return [s]
        s_list = []
        if self.fuhe(s):
            s_list.append(s)
        for i in range(1, len(s)):
            a = s[:i] + '.' + s[i:]
            if self.fuhe(a):
                s_list.append(a)
        return s_list

    def ambiguousCoordinates(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        s = S[1:-1]

        dou_list = []
        for i in range(1, len(s)):
            dou_list.append([s[:i], s[i:]])

        dian_list = []
        for i in dou_list:
            x, y = i
            x_list = self.num_list_after_add_dian(x)
            y_list = self.num_list_after_add_dian(y)
            dian_list.extend(['(' + xx + ', ' + yy + ')' for xx in x_list for yy in y_list])
        return dian_list


a = Solution().ambiguousCoordinates('(00011)')
print (a)