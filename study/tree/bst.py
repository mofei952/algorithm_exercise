#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/5/23 18:04
# @File    : bst.py
# @Software: PyCharm
import random

from study.tree.tree_node import TreeNode


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = TreeNode(val)
            return
        node = self.root
        t = None
        while node:
            t = node
            if val < node.val:
                node = node.left
            else:
                node = node.right
        if val < t.val:
            t.left = TreeNode(val)
        else:
            t.right = TreeNode(val)

    def inorderTraversal(self):
        stack = []
        node = self.root
        res = []
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                t = stack.pop()
                res.append(t.val)
                if t.right:
                    node = t.right
        return res


if __name__ == '__main__':
    bst = BinarySearchTree()
    # bst.insert(5)
    # bst.insert(4)
    # bst.insert(2)
    # bst.insert(3)
    # bst.insert(6)
    # bst.insert(1)
    # print(bst.inorderTraversal())
    for i in range(100):
        bst.insert(random.randint(1, 100))
    print(bst.inorderTraversal())
