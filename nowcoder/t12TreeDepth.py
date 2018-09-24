#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/9/24 23:08
# @File    : t12TreeDepth.py
# @Software: PyCharm

# 二叉树的深度
# https://www.nowcoder.com/practice/435fb86331474282a3499955f0a41e8b?tpId=13&tqId=11191&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def TreeDepth(self, pRoot):
        if pRoot is None:
            return 0
        return max(self.TreeDepth(pRoot.left), self.TreeDepth(pRoot.right))+1

node = TreeNode(0)
node1 = TreeNode(1)
node2 = TreeNode(2)
node.left = node1
node1.left = node2
print(Solution().TreeDepth(node))