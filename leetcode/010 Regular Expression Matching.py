#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/9/17 19:53
# @File    : 010 Regular Expression Matching.py
# @Software: PyCharm

"""
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.
'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:
s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.

Example 1:
Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:
Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the precedeng element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

Example 3:
Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".

Example 4:
Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore it matches "aab".

Example 5:
Input:
s = "mississippi"
p = "mis*is*p*."
Output: false
"""


class Solution(object):
    def isMatch(self, s, p):
        """
        字符串s和pattern是否正则匹配
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


if __name__ == '__main__':
    result = Solution().isMatch('aab', 'c*a*b*')
    print(result)
