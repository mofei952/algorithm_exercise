#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/10/27 15:28
# @File    : 007 Reverse Integer.py
# @Software: PyCharm

"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1].
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""


class Solution:
    def reverse(self, x):
        """
        反转整型变量的数字
        :type x: int
        :rtype: int
        """
        sign = -1 if x < 0 else 1
        x *= sign
        result = 0
        while x:
            r = x % 10
            x = x // 10
            result = result * 10 + r
        result *= sign
        if result < -2 ** 31 or result > 2 ** 31 - 1:
            return 0
        return result

    def reverse2(self, x):
        """
        反转整型变量的数字， 通过转换为字符串再反转实现
        :type x: int
        :rtype: int
        """
        sign = -1 if x < 0 else 1
        x *= sign
        s = str(x)
        result = 0
        for i in s[::-1]:
            result = result * 10 + (ord(i)-ord('0'))
        result *= sign
        if result < -2 ** 31 or result > 2 ** 31 - 1:
            return 0
        return result


if __name__ == '__main__':
    result = Solution().reverse2(1534236469)
    print(result)
