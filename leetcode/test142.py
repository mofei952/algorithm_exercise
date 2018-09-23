#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/9/23 14:32
# @File    : test142.py
# @Software: PyCharm

# 链表中环的入口结点
# https://leetcode.com/problems/linked-list-cycle-ii/description/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        s = set()
        while head is not None:
            if head in s:
                return head
            s.add(head)
            head = head.next
        return None
