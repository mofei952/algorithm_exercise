#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/9/25 12:49
# @File    : t16PrintTree.py
# @Software: PyCharm

# 把二叉树打印成多行
# https://www.nowcoder.com/practice/445c44d982d04483b04a54f298796288?tpId=13&tqId=11213&tPage=2&rp=2&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking
from utils import create_tree


class Solution:
    # 返回二维列表[[1,2],[4,5]]
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
        return ret


r = create_tree([1, 2, 3, 4, 5, None, 6, 7])
print(Solution().Print(r))
