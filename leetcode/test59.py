#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/8/23 9:25
# @File    : test59.py
# @Software: PyCharm

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        dir = 0
        matrix = [[0 for i in range(n)] for i in range(n)]
        x, y = 0, 0
        num = 1
        while True:
            matrix[x][y] = num
            dx, dy = dirs[dir]
            xx = x + dx
            yy = y + dy
            if xx >= 0 and xx < len(matrix) and yy >= 0 and yy < len(matrix[xx]) and matrix[xx][yy] == 0:
                x = xx
                y = yy
            else:
                dir = (dir + 1) % 4
                dx, dy = dirs[dir]
                xx = x + dx
                yy = y + dy
                if xx >= 0 and xx < len(matrix) and yy >= 0 and yy < len(matrix[xx]) and matrix[xx][yy] == 0:
                    x = xx
                    y = yy
                else:
                    return matrix
            num += 1

        return matrix


a = Solution().generateMatrix(10)
for i in a:
    print (i)
