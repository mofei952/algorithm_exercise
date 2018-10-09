#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/10/1 22:24
# @File    : test230.py
# @Software: PyCharm


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from nowcoder.utils import create_tree


class Solution:
    ret = None
    n = 1

    def mid(self, root, k):
        if not root:
            return
        if self.n > k:
            return
        self.mid(root.left, k)
        if self.n == k and self.ret is None:
            self.ret = root.val
            return
        else:
            self.n += 1
        self.mid(root.right, k)

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if not root:
            return None
        self.ret = None
        self.n = 1
        self.mid(root, k)
        return self.ret

    def kthSmallest2(self, root, k):
        stack = []
        node = root
        while node:
            stack.append(node)
            node = node.left
        count = 0
        while stack:
            node = stack.pop()
            count += 1
            if count == k:
                break
            node = node.right
            while node:
                stack.append(node)
                node = node.left
        if count == k:
            return node.val
        else:
            return None

a = create_tree(
    [31, 30, 48, 3, None, 38, 49, 0, 16, 35, 47, None, None, None, 2, 15, 27, 33, 37, 39, None, 1, None, 5, None, 22,
     28, 32, 34, 36, None, None, 43, None, None, 4, 11, 19, 23, None, 29, None, None, None, None, None, None, 40, 46,
     None, None, 7, 14, 17, 21, None, 26, None, None, None, 41, 44, None, 6, 10, 13, None, None, 18, 20, None, 25, None,
     None, 42, None, 45, None, None, 8, None, 12, None, None, None, None, None, 24, None, None, None, None, None, None,
     9])
print(Solution().kthSmallest(a, 100000))
print(Solution().kthSmallest2(a, 100000))
