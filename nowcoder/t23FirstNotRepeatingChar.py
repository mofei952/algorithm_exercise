#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/10/20 23:07
# @File    : t23FirstNotRepeatingChar.py
# @Software: PyCharm


# 第一个只出现一次的字符
# https://www.nowcoder.com/practice/1c82e8cf713b4bbeb2a5b31cf5b0417c?tpId=13&tqId=11187&tPage=2&rp=2&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking

class Solution:
    def FirstNotRepeatingChar(self, s):
        if not s:
            return -1
        dict = {}
        list = []
        for i in s:
            if i not in dict:
                dict[i] = 1
                list.append(i)
            else:
                dict[i] += 1
                if dict[i] == 2:
                    list.remove(i)
        return s.index(list[0])


print(Solution().FirstNotRepeatingChar(''))
