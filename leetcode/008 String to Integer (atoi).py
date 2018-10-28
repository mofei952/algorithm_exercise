#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/10/27 16:57
# @File    : 008 String to Integer (atoi).py
# @Software: PyCharm

"""
Implement atoi which converts a string to an integer.
The function first discards as many whitespace characters as necessary until the first non-whitespace character is found.
Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible,
and interprets them as a numerical value.
The string can contain additional characters after those that form the integral number,
which are ignored and have no effect on the behavior of this function.
If the first sequence of non-whitespace characters in str is not a valid integral number,
or if no such sequence exists because either str is empty or it contains only whitespace characters,
no conversion is performed.
If no valid conversion could be performed, a zero value is returned.

Note:
Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.

Example 1:
Input: "42"
Output: 42

Example 2:
Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.

Example 3:
Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.

Example 4:
Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical
             digit or a +/- sign. Therefore no valid conversion could be performed.

Example 5:
Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Thefore INT_MIN (−231) is returned.
"""


class Solution:
    def myAtoi(self, str):
        """
        字符串转数字
        :type str: str
        :rtype: int
        """
        str = str.lstrip()
        signs = ['+', '-']
        if not str or str[0] not in signs and not '0' <= str[0] <= '9':
            return 0
        index = 0
        sign = 1
        if str[0] in signs:
            index += 1
            if str[0] == '-':
                sign = -1
        result = 0
        for i in range(index, len(str)):
            if not '0' <= str[i] <= '9':
                break
            result = result * 10 + ord(str[i]) - ord('0')
        result *= sign
        if result > 2 ** 31 - 1:
            result = 2 ** 31 - 1
        elif result < -2 ** 31:
            result = -2 ** 31
        return result


if __name__ == '__main__':
    result = Solution().myAtoi('4193 with words')
    print(result)
