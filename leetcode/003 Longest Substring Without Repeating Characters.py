#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/10/26 21:52
# @File    : 003 Longest Substring Without Repeating Characters.py
# @Software: PyCharm

"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:
Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {}
        max_length = 0
        start = 0
        for index, val in enumerate(s):
            start = max(dict[val] + 1 if val in dict else 0, start)
            max_length = max(max_length, index - start + 1)
            dict[val] = index
        return max_length


if __name__ == '__main__':
    result = Solution().lengthOfLongestSubstring('dvdf')
    print(result)
