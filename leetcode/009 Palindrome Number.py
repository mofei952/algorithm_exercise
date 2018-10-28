#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/10/28 14:35
# @File    : 009 Palindrome Number.py
# @Software: PyCharm

"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:
Input: 121
Output: true

Example 2:
Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""


class Solution:
    def isPalindrome(self, x):
        """
        是否回文数字
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x < 10:
            return True
        if x % 10 == 0:
            return False
        reverse = 0
        t = x
        while t:
            reverse = reverse * 10 + t % 10
            if reverse > x:
                return False
            t //= 10
        return reverse == x


if __name__ == '__main__':
    result = Solution().isPalindrome(0)
    print(result)
