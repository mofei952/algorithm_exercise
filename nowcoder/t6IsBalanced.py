#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/9/24 17:29
# @File    : t6IsBalanced.py
# @Software: PyCharm

# 是否是平衡二叉树
# https://www.nowcoder.com/practice/8b3b95850edb4115918ecebdf1b4d222?tpId=13&tqId=11192&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def height(self, node):
        if node is None:
            return 0
        return max(self.height(node.left), self.height(node.right)) + 1

    def IsBalanced_Solution(self, pRoot):
        if pRoot is None:
            return True
        if self.IsBalanced_Solution(pRoot.left) \
                and self.IsBalanced_Solution(pRoot.right) \
                and abs(self.height(pRoot.left) - self.height(pRoot.right)) <= 1:
            return True
        return False

root = TreeNode(0)
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
root.left = node1
root.right = node2
node1.left = node3
node3.left = node4
print(Solution().IsBalanced_Solution(root))