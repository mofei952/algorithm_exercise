#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/11/1 10:15
# @File    : 048 Rotate Image.py
# @Software: PyCharm

"""
You are given an n x n 2D matrix representing an image.
Rotate the image by 90 degrees (clockwise).

Note:
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:
Given input matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],
rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]

Example 2:
Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
],
rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
"""


class Solution:
    def rotate(self, matrix):
        """
        返回一个新矩阵，可以实现m*n矩阵的旋转
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return []
        m = len(matrix)
        n = len(matrix[0])
        result = [[0 for j in range(m)] for i in range(n)]
        for i in range(n):
            for j in range(m):
                result[i][j] = matrix[m - j - 1][i]
        return result

    def rotate2(self, matrix):
        """
        旋转矩阵，修改原有的矩阵，不返回
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        n = len(matrix)
        visited = {}
        for i in range(n):
            for j in range(n):
                if (i, j) in visited:
                    continue
                t = matrix[i][j]
                for k in range(4):
                    visited[(i, j)] = 1
                    if k == 3:
                        matrix[i][j] = t
                    else:
                        matrix[i][j] = matrix[n - j - 1][i]
                    i, j = n - j - 1, i


if __name__ == '__main__':
    matrix = [
        [5, 1, 9, 11],
        [2, 4, 8, 10],
        [13, 3, 6, 7],
        [15, 14, 12, 16]
    ]
    # matrix = Solution().rotate(matrix)
    Solution().rotate2(matrix)
    for i in matrix:
        print(i)
