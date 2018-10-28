#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/9/1 17:34
# @File    : 014 Longest Common Prefix.py
# @Software: PyCharm

"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Note:
All given inputs are in lowercase letters a-z.
"""


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        最长相同前缀字符串
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        result = strs[0]
        for i in range(1, len(strs)):
            s = strs[i]
            common_s = ''
            for j in range(min(len(s), len(result))):
                if s[j] == result[j]:
                    common_s += s[j]
                else:
                    break
            result = common_s
        return result

    def longestCommonPrefix2(self, strs):
        """
        最长相同前缀字符串
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        min_length = min(len(str) for str in strs)
        for length in range(min_length, -1, -1):
            s = strs[0][:length]
            count = 0
            for str in strs:
                if str[:length] != s:
                    break
                count += 1
            if count == len(strs):
                return s
        return ''


if __name__ == '__main__':
    result = Solution().longestCommonPrefix2(["dog", "racecar", "car"])
    print(result, '1')
