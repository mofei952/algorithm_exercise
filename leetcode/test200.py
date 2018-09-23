#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/8/23 16:37
# @File    : test200.py
# @Software: PyCharm

class Solution(object):
    def dfs(self, grid, x, y):
        if x >= 0 and x < len(grid) and y >= 0 and y < len(grid[x]) and grid[x][y] == '1':
            grid[x][y] = '#'
            self.dfs(grid, x, y - 1)
            self.dfs(grid, x, y + 1)
            self.dfs(grid, x - 1, y)
            self.dfs(grid, x + 1, y)

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count


s = """11110
11010
11000
00000"""
a = []
for i in s.split('\n'):
    a.append(i)
for i in range(len(a)):
    b = []
    for j in a[i]:
        b.append(j)
    a[i] = b
print(a) 

c = Solution().numIslands(a)
print(c)
