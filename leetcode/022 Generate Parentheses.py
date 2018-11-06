#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/11/6 12:37
# @File    : 022 Generate Parentheses.py
# @Software: PyCharm

"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""


class Solution:
    def generateParenthesis(self, n):
        """
        生成n对括号的所有组合
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return []
        result = []
        def generate(s, left, right):
            if left == n and right == n:
                result.append(s[:])
                return
            if left == n:
                generate(s + ')', left, right + 1)
            elif left == right:
                generate(s + '(', left + 1, right)
            elif left > right:
                generate(s + '(', left + 1, right)
                generate(s + ')', left, right + 1)
        generate('', 0, 0)
        return result


if __name__ == '__main__':
    result = Solution().generateParenthesis(3)
    print(result)
