#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/9/26 21:37
# @File    : test297.py
# @Software: PyCharm

# 序列化和反序列化二叉树
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return []
        queue = [root]
        ret = []
        while queue:
            node = queue.pop(0)
            if node:
                ret.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                ret.append(None)
        index = len(ret) - 1
        while ret[index] is None:
            ret.pop(index)
            index -= 1
        return ret

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        root = TreeNode(data[0])
        queue = [root]
        node = None
        flag = True
        for i in data[1:]:
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


r = Codec().deserialize([1, 2, 3, None, None, 4, 5])
print(r)
data = Codec().serialize(r)
print(data)
