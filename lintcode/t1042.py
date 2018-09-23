#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/6/28 10:21
# @File    : t1042.py
# @Software: PyCharm
class Solution:
    """
    @param matrix: the given matrix
    @return: True if and only if the matrix is Toeplitz
    """

    def isToeplitzMatrix(self, matrix):
        # Write your code here
        row = len(matrix)
        col = len(matrix[0])
        heads = []
        for i in range(0, col):
            heads.append((0, i))
        for i in range(1, row):
            heads.append((i, 0))
        for head in heads:
            ro = head[0]
            co = head[1]
            t = matrix[ro][co]
            r = ro
            c = co
            while r + 1 < row and c + 1 < col:
                r = r + 1
                c = c + 1
                if matrix[r][c] != t:
                    return False

        return True