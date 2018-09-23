#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/9/1 17:34
# @File    : test14.py
# @Software: PyCharm

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        result = strs[0]
        for i in range(len(strs)):
            s = strs[i]
            common_s = ''
            for j in range(min(len(s), len(result))):
                if s[j] == result[j]:
                    common_s += s[j]
                else:
                    break
            result = common_s
        return result

a = Solution().longestCommonPrefix(["dog","racecar","car"])
print(a)