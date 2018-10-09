#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/10/9 19:04
# @File    : test106.py
# @Software: PyCharm

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not postorder:
            return None
        val = postorder[-1]
        index = inorder.index(val)
        left_inorder = inorder[:index]
        right_inorder = inorder[index + 1:]
        left_postorder = postorder[0: len(left_inorder)]
        right_postorder = postorder[len(left_inorder):-1]
        node = TreeNode(val)
        node.left = self.buildTree(left_inorder, left_postorder)
        node.right = self.buildTree(right_inorder, right_postorder)
        return node


a = Solution().buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3])
print(a)
