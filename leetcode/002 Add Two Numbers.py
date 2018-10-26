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


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        list = [self.val]
        t = self
        while t.next:
            t = t.next
            list.append(t.val)
        return '->'.join(str(i) for i in list)


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        对应位置相加，超过十进行进位操作
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = None
        t1 = l1
        t2 = l2
        r = None
        d = 0
        while t1 or t2:
            if not result:
                r = result = ListNode(0)
            else:
                r.next = ListNode(0)
                r = r.next
            val1 = t1.val if t1 else 0
            val2 = t2.val if t2 else 0
            d, r.val = divmod(val1 + val2 + d, 10)
            if t1:
                t1 = t1.next
            if t2:
                t2 = t2.next
        if d:
            r.next = ListNode(0)
            r.next.val = d
        return result


if __name__ == '__main__':
    l1s = [ListNode(1), ListNode(1)]
    l2s = [ListNode(9), ListNode(9)]
    for i in range(len(l1s) - 1):
        l1s[i].next = l1s[i + 1]
    for i in range(len(l2s) - 1):
        l2s[i].next = l2s[i + 1]
    result = Solution().addTwoNumbers(l1s[0], l2s[0])
    print(result)
