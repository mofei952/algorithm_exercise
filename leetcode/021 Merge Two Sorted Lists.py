#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/6/27 17:33
# @File    : 021 Merge Two Sorted Lists.py
# @Software: PyCharm

"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""
from utils import ListNode


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        合并两个有序链表
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        t1 = l1
        t2 = l2
        cur = head = ListNode(0)
        while t1 or t2:
            if not t1:
                cur.next = ListNode(t2.val)
                t2 = t2.next
            elif not t2:
                cur.next = ListNode(t1.val)
                t1 = t1.next
            elif t1.val < t2.val:
                cur.next = ListNode(t1.val)
                t1 = t1.next
            else:
                cur.next = ListNode(t2.val)
                t2 = t2.next
            cur = cur.next
        return head.next


if __name__ == '__main__':
    list1 = ListNode.create_linked_list([2, 3])
    list2 = ListNode.create_linked_list([1, 2])
    result = Solution().mergeTwoLists(list1, list2)
    print(result)
