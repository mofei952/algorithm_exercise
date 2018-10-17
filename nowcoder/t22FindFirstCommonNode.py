#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/10/12 14:59
# @File    : t22FindFirstCommonNode.py
# @Software: PyCharm

# 两个链表的第一个公共结点
# https://www.nowcoder.com/practice/6ab1d9a29e88450685099d45c9e31e46?tpId=13&tqId=11189&tPage=2&rp=2&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def length(self, head):
        t = head
        count = 0
        while t is not None:
            t = t.next
            count += 1
        return count

    def FindFirstCommonNode(self, pHead1, pHead2):
        t1 = pHead1
        t2 = pHead2
        l1 = self.length(pHead1)
        l2 = self.length(pHead2)
        if l1 < l2:
            t1, t2 = t2, t1
        for i in range(abs(l2 - l1)):
            t1 = t1.next
        result = None
        while t1 is not None and t2 is not None:
            if t1 == t2:
                result = t1
                break
            t1 = t1.next
            t2 = t2.next
        return result


node = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node.next = node2
node2.next = node3
node4.next = node2

print(Solution().FindFirstCommonNode(node, node4).val)
