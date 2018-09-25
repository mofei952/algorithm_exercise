#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/9/25 11:44
# @File    : t15GetNext.py
# @Software: PyCharm


class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    def GetNext(self, pNode):
        if pNode is None:
            return None
        if pNode.right:
            pNode = pNode.right
            while pNode.left:
                pNode = pNode.left
            return pNode
        if not pNode.next:
            return None
        p = pNode
        t = pNode.next
        while t and t.left != p:
            p = t
            t = t.next
        return t


node = TreeLinkNode(8)
node2 = TreeLinkNode(6)
node3 = TreeLinkNode(10)
node4 = TreeLinkNode(5)
node5 = TreeLinkNode(7)
node6 = TreeLinkNode(9)
node7 = TreeLinkNode(11)
node.left = node2
node2.next = node
node.right = node3
node3.next = node
node2.left = node4
node4.next = node2
node2.right = node5
node5.next = node2
node3.left = node6
node6.next = node3
node3.right = node7
node7.next = node3
# 13024
print(Solution().GetNext(node).val)
