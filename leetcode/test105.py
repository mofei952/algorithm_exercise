#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/10/7 15:22
# @File    : test105.py
# @Software: PyCharm


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None
        val = preorder[0]
        index = inorder.index(val)
        left_inorder = inorder[:index]
        right_inorder = inorder[index + 1:]
        left_preorder = preorder[1:len(left_inorder)+1]
        right_preorder = preorder[1 + len(left_inorder):]
        node = TreeNode(val)
        node.left = self.buildTree(left_preorder, left_inorder)
        node.right = self.buildTree(right_preorder, right_inorder)
        return node


a = Solution().buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
print(a)
