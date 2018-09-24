#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/9/24 23:03
# @File    : t11ReverseSentence.py
# @Software: PyCharm

# 翻转单词顺序列
# https://www.nowcoder.com/practice/3194a4f4cf814f63919d0790578d51f3?tpId=13&tqId=11197&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking

class Solution:
    def ReverseSentence(self, s):
        str_list = s.split(' ')
        str_list.reverse()
        return ' '.join(str_list)

print(Solution().ReverseSentence('124 81 asd'))
