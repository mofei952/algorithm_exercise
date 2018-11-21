#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/11/12 21:50
# @File    : 023 Merge k Sorted Lists.py
# @Software: PyCharm

"""
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:
Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"

Example 2:
Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
"""


class Solution:
    def longestValidParentheses(self, s):
        """
        最长的有效括号子串长度
        :type s: str
        :rtype: int
        """
        stack = []
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                if stack and s[stack[-1]] == '(':
                    stack.pop()
                else:
                    stack.append(i)
        stack.insert(0, -1)
        stack.append(len(s))
        longest = 0
        for i in range(1, len(stack)):
            num = stack[i] - stack[i - 1] - 1
            longest = max(longest, num)
        return longest


if __name__ == '__main__':
    result = Solution().longestValidParentheses("()")
    print(result)
