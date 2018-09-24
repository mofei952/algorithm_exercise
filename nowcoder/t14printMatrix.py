#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/9/24 23:15
# @File    : t14printMatrix.py
# @Software: PyCharm

# 顺时针打印矩阵
# https://www.nowcoder.com/practice/9b4c81a02cd34f76be2659fa0d54342a?tpId=13&tqId=11172&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking

class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        ret = []
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        pos = [0, 0]
        dir_index = 0
        for i in range(len(matrix) * len(matrix[0])):
            r = pos[0]
            c = pos[1]
            ret.append(matrix[r][c])
            matrix[r][c] = -1
            dir = dirs[dir_index]
            next_pos = list(map(lambda x, y: x + y, dir, pos))
            next_r = next_pos[0]
            next_c = next_pos[1]
            if next_pos[0] < 0 or next_pos[0] >= len(matrix)\
                    or next_pos[1] < 0 or next_pos[1] >= len(matrix[0]) \
                    or matrix[next_r][next_c] == -1:
                dir_index = (dir_index + 1) % 4
                dir = dirs[dir_index]
                next_pos = list(map(lambda x, y: x + y, dir, pos))
            pos = next_pos
        return ret

print(Solution().printMatrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]))
