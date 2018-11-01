#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/9/25 12:08
# @File    : 101 Symmetric Tree.py
# @Software: PyCharm

"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
"""

from utils import create_tree


class Solution(object):
    def symmetric(self, l, r):
        if not l and not r:
            return True
        elif l and r:
            return l.val == r.val and self.symmetric(l.left, r.right) and self.symmetric(l.right, r.left)
        else:
            return False

    def isSymmetric(self, root):
        """
        二叉树是否对称
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.symmetric(root.left, root.right)

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
        二叉树是否对称，先反转左子树，再比较左右子树是否相同
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        left2 = self.reverse(root.left)
        return self.same(left2, root.right)

if __name__ == '__main__':
    tree = create_tree([1, 2, 2, 3, 4, 4, 3])
    result = Solution().isSymmetric(tree)
    print(result)
