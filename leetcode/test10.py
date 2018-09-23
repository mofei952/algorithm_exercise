#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/9/17 19:53
# @File    : test10.py
# @Software: PyCharm


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if p == '':
            return s == ''
        if len(p) > 1 and p[1] == '*':
            # x*匹配0个字符
            if self.isMatch(s, p[2:]):
                return True
            # x*先匹配1个字符
            if s != '' and (s[0] == p[0] or p[0] == '.') and self.isMatch(s[1:], p):
                return True
        else:
            if s != '' and (s[0] == p[0] or p[0] == '.') and self.isMatch(s[1:], p[1:]):
                return True
        return False

a = Solution().isMatch('aab', 'c*a*b*')
print(a)