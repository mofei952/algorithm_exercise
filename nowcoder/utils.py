#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/9/25 12:56
# @File    : utils.py
# @Software: PyCharm


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def create_tree(list):
    if not list:
        return None
    root = TreeNode(list[0])
    queue = [root]
    node = None
    flag = True
    for i in list[1:]:
        if flag:
            node = queue.pop(0)
            if i is not None:
                node.left = TreeNode(i)
                queue.append(node.left)
            flag = False
        else:
            if i is not None:
                node.right = TreeNode(i)
                queue.append(node.right)
            flag = True
    return root
