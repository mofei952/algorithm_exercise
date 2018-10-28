#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/10/27 12:12
# @File    : 005 Longest Palindromic Substring.py
# @Software: PyCharm

"""
Given a string s, find the longest palindromic substring in s.
You may assume that the maximum length of s is 1000.

Example 1:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: "cbbd"
Output: "bb"
"""


class Solution:
    def longestPalindrome(self, s):
        """
        最长回文子串
        :type s: str
        :rtype: str
        """
        if not s:
            return ''
        result = s[0]
        for i in range(len(s)):
            ss = self.longest_palindrome_from_center(s, i - 1, i + 1)
            if len(ss) > len(result):
                result = ss
            if i + 1 < len(s) and s[i] == s[i + 1]:
                ss = self.longest_palindrome_from_center(s, i - 1, i + 2)
                if len(ss) > len(result):
                    result = ss
        return result

    def longest_palindrome_from_center(self, s, l, r):
        while l >= 0 and r < len(s):
            if s[l] == s[r]:
                l -= 1
                r += 1
            else:
                break
        return s[l + 1: r]


if __name__ == '__main__':
    result = Solution().longestPalindrome('cbbd')
    print(result)
