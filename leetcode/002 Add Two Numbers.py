#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/10/26 21:14
# @File    : 002 Add Two Numbers.py
# @Software: PyCharm

"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""
from utils import ListNode


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        将两个链表形式的数字相加
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        t1 = l1
        t2 = l2
        cur = head = ListNode(0)
        d = 0
        while t1 or t2:
            cur.next = ListNode(0)
            cur = cur.next
            val1 = t1.val if t1 else 0
            val2 = t2.val if t2 else 0
            d, cur.val = divmod(val1 + val2 + d, 10)
            if t1:
                t1 = t1.next
            if t2:
                t2 = t2.next
        if d:
            cur.next = ListNode(d)
        return head.next


if __name__ == '__main__':
    l1 = ListNode.create_linked_list([1, 1])
    l2 = ListNode.create_linked_list([9, 9])
    result = Solution().addTwoNumbers(l1, l2)
    print(result)
