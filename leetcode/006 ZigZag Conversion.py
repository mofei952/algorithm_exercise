#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/10/27 14:23
# @File    : 006 ZigZag Conversion.py
# @Software: PyCharm

"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
(you may want to display this pattern in a fixed font for better legibility)
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:
string convert(string s, int numRows);

Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
"""


class Solution:
    def convert(self, s, numRows):
        """
        z形状列表转换为正常显示
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 0:
            return ''
        if numRows == 1:
            return s
        d = (numRows - 1) * 2
        list = [index for index in range(0, len(s) + d, d)]
        hash_set = set(list)
        i = 0
        while i < len(list):
            index = list[i]
            if index - 1 >= 0 and index - 1 not in hash_set:
                list.append(index - 1)
                hash_set.add(index-1)
            if index + 1 < len(s) and index + 1 not in hash_set:
                list.append(index + 1)
                hash_set.add(index + 1)
            i += 1
        return ''.join(s[index] for index in list if index < len(s))

    def convert2(self, s, numRows):
        """
        z形状列表转换为正常显示, 通过分别统计每行的字母实现
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 0:
            return ''
        if numRows == 1:
            return s
        dict = {}
        row = 1
        step = 1
        # 分别统计每行的字母
        for v in s:
            if row not in dict:
                dict[row] = []
            dict[row].append(v)
            row += step
            if row == 1 or row == numRows:
                step *= -1
        result = ''
        for i in range(1, numRows+1):
            if i in dict:
                result += ''.join(dict[i])
        return result

if __name__ == '__main__':
    result = Solution().convert2('PAYPALISHIRING', 4)
    print(result)
    assert result == 'PINALSIGYAHRPI'
