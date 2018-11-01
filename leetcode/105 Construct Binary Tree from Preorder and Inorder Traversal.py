#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/10/7 15:22
# @File    : 105 Construct Binary Tree from Preorder and Inorder Traversal.py
# @Software: PyCharm

"""
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:
    3
   / \
  9  20
    /  \
   15   7
"""
from utils import TreeNode


class Solution:
    def buildTree(self, preorder, inorder):
        """
        根据先序遍历和中序遍历，构造二叉树
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
            return None
        val = preorder[0]
        index = inorder.index(val)
        left_inorder = inorder[:index]
        right_inorder = inorder[index + 1:]
        left_preorder = preorder[1:len(left_inorder) + 1]
        right_preorder = preorder[1 + len(left_inorder):]
        node = TreeNode(val)
        node.left = self.buildTree(left_preorder, left_inorder)
        node.right = self.buildTree(right_preorder, right_inorder)
        return node

    def buildTree2(self, preorder, inorder):
        """
        根据先序遍历和中序遍历，构造二叉树
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
            return None
        dict = {}
        for i, v in enumerate(inorder):
            dict[v] = i
        def buildTree_recursive(preorder_start, preorder_end, inorder_start, inorder_end):
            if preorder_end < preorder_start or inorder_end < inorder_start:
                return None
            val = preorder[preorder_start]
            node = TreeNode(val)
            index = dict[val]
            node.left = buildTree_recursive(preorder_start + 1, preorder_start + (index - inorder_start), inorder_start,
                                            index - 1)
            node.right = buildTree_recursive(preorder_start + (index - inorder_start) + 1, preorder_end, index + 1,
                                             inorder_end)
            return node
        tree = buildTree_recursive(0, len(preorder) - 1, 0, len(inorder) - 1)
        return tree


if __name__ == '__main__':
    tree = Solution().buildTree2([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
    print(tree)
