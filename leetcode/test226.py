#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/9/23 14:10
# @File    : test226.py
# @Software: PyCharm

# 二叉树的镜像
# https://leetcode.com/problems/invert-binary-tree/description/

# Definition for a binary tree node.
from utils import create_tree


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

t = create_tree([4, 2, 7, 1, 3, 6, 9])
t = Solution().invertTree(t)
print(t)
