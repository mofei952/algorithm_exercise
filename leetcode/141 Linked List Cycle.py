#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/9/23 14:35
# @File    : test141.py
# @Software: PyCharm

"""
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
"""
from utils import ListNode


class Solution(object):
    def hasCycle(self, head):
        """
        判断链表是否有环
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

    def hasCycle2(self, head):
        """
        判断链表是否有环，O(1)空间复杂度
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        fast = head
        slow = head
        while fast and fast.next and slow:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False


if __name__ == '__main__':
    head = ListNode.create_linked_list([1, 2])
    # head.next.next.next = head
    res = Solution().hasCycle2(head)
    print(res)
