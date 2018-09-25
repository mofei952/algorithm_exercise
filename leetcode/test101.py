#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/9/25 12:08
# @File    : test101.py
# @Software: PyCharm

# 对称的二叉树
# https://leetcode.com/problems/symmetric-tree/description/
from nowcoder.utils import create_tree


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def reverse(self, node):
        if not node:
            return
        node.left, node.right = node.right, node.left
        self.reverse(node.left)
        self.reverse(node.right)
        return node

    def same(self, l, r):
        if not l and not r:
            return True
        elif l and r:
            return l.val == r.val and self.same(l.left, r.left) and self.same(l.right, r.right)
        else:
            return False

    def isSymmetric2(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        left2 = self.reverse(root.left)
        return self.same(left2, root.right)

    def symmetric(self, l, r):
        if not l and not r:
            return True
        elif l and r:
            return l.val == r.val and self.symmetric(l.left, r.right) and self.symmetric(l.right, r.left)
        else:
            return False

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.symmetric(root.left, root.right)

r = create_tree([1, 2, 2, 3, 4, 4, 3])
print(Solution().isSymmetric2(r))
