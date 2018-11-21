#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/9/23 14:32
# @File    : test142.py
# @Software: PyCharm

"""
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Note: Do not modify the linked list.

Follow up:
Can you solve it without using extra space?
"""
from utils import ListNode


class Solution(object):
    def detectCycle(self, head):
        """
        检测链表是否有环
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

    def detectCycle2(self, head):
        """
        检测链表是否有环，O(1)空间复杂度
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return None
        fast = head
        slow = head
        while fast and fast.next and slow:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        if not fast or not fast.next:
            return None
        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return fast


if __name__ == '__main__':
    head = ListNode.create_linked_list([1, 2, 3])
    # head.next.next.next = head
    res = Solution().detectCycle2(head)
    print(res is not None)
