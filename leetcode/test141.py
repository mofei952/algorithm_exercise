#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/9/23 14:35
# @File    : test141.py
# @Software: PyCharm

# 链表中是否有环
# https://leetcode.com/problems/linked-list-cycle/description/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        s = set()
        while head is not None:
            if head in s:
                return True
            s.add(head)
            head = head.next
        return False
