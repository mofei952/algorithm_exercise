#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/8/23 9:25
# @File    : 059 Spiral Matrix II.py
# @Software: PyCharm

"""
Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:
Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""


class Solution(object):
    def generateMatrix(self, n):
        """
        生成螺旋顺序的矩阵
        :type n: int
        :rtype: List[List[int]]
        """
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dir_index = 0
        matrix = [[0 for i in range(n)] for i in range(n)]
        x, y = 0, 0
        num = 1
        for i in range(n * n):
            matrix[x][y] = num
            dx, dy = dirs[dir_index]
            xx = x + dx
            yy = y + dy
            if 0 <= xx < len(matrix) and 0 <= yy < len(matrix[xx]) and matrix[xx][yy] == 0:
                x = xx
                y = yy
            else:
                dir_index = (dir_index + 1) % 4
                dx, dy = dirs[dir_index]
                x += dx
                y += dy
            num += 1
        return matrix


if __name__ == '__main__':
    result = Solution().generateMatrix(10)
    for i in result:
        print(i)
