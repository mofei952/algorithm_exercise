#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/9/25 22:51
# @File    : t17PrintTree2.py
# @Software: PyCharm

# 按之字形顺序打印二叉树
# https://www.nowcoder.com/practice/91b69814117f4e8097390d107d2efbe0?tpId=13&tqId=11212&tPage=2&rp=2&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking
from utils import create_tree


class Solution:
    def Print(self, pRoot):
        if not pRoot:
            return []
        level = 0
        ret = [[]]
        t = []
        t.append([pRoot, 0])
        while t:
            node = t.pop(0)
            if not node[0]:
                continue
            if node[1] != level:
                ret.append([])
                level = node[1]
            ret[level].append(node[0].val)
            t.append([node[0].left, node[1] + 1])
            t.append([node[0].right, node[1] + 1])
        for row in ret[1::2]:
            row.reverse()
        return ret


r = create_tree([1, 2, 3, 4, 5, None, 6, 7, 8])
print(Solution().Print(r))
