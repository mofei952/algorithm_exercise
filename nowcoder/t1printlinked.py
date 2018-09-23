#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/9/23 15:25
# @File    : printlinked.py
# @Software: PyCharm

# 从尾到头打印链表
# https://www.nowcoder.com/practice/d0267f7f55b3412ba93bd35cfa8e8035?tpId=13&tqId=11156&tPage=1&rp=1&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        list = []
        temp = listNode
        while temp is not None:
            list.append(temp.val)
            temp = temp.next
        list.reverse()
        return list


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
a.next = b
b.next = c
res = Solution().printListFromTailToHead(a)
print(res)
