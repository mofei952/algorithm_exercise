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


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    @classmethod
    def create_linkedlist(cls, nums):
        if not nums:
            return None
        root = cls(nums[0])
        temp = root
        for i in nums[1:]:
            temp.next = cls(i)
            temp = temp.next
        return root

    def __str__(self):
        list = [self.val]
        t = self
        while t.next:
            t = t.next
            list.append(t.val)
        return '->'.join(str(i) for i in list)


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
    list1 = ListNode.create_linkedlist([2, 3])
    list2 = ListNode.create_linkedlist([1, 2])
    result = Solution().mergeTwoLists(list1, list2)
    print(result)
