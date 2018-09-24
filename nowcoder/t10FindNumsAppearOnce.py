#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/9/24 18:16
# @File    : t10FindNumsAppearOnce.py
# @Software: PyCharm

# 数组中只出现一次的数字
# https://www.nowcoder.com/practice/e02fdb54d7524710a7d664d082bb7811?tpId=13&tqId=11193&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking


class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        c_dict = {}
        for i in array:
            if i not in c_dict:
                c_dict[i] = 1
            else:
                del c_dict[i]
        return list(c_dict.keys())


print(Solution().FindNumsAppearOnce([1, 2, 3, 3]))
