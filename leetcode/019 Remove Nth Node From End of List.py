#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/11/12 19:59
# @File    : 019 Remove Nth Node From End of List.py
# @Software: PyCharm

"""
Given a linked list, remove the n-th node from the end of list and return its head.

Example:
Given linked list: 1->2->3->4->5, and n = 2.
After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:
Given n will always be valid.

Follow up:
Could you do this in one pass?
"""
from utils import ListNode


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        nodes = []
        t = head
        while t:
            nodes.append(t)
            t = t.next
        if n > len(nodes) or n < 1:
            return head
        if n == 1:
            node = None
        else:
            node = nodes[-n + 1]
        if n == len(nodes):
            head = node
        else:
            nodes[-n - 1].next = node
        return head


if __name__ == '__main__':
    linked_list = ListNode.create_linked_list([1, 2, 3, 4, 5])
    result = Solution().removeNthFromEnd(linked_list, 5)
    print(result)
