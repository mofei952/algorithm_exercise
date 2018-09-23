#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/6/27 17:33
# @File    : test.py
# @Software: PyCharm

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        t1 = l1
        t2 = l2
        v1 = None
        v2 = None
        arr = []
        while t1 != None or t2 != None:
            if t1 != None and v1 == None:
                v1 = t1.val
                t1 = t1.next
            if t2 != None and v2 == None:
                v2 = t2.val
                t2 = t2.next
            if v1 == None or v2 == None:
                break
            if v1 < v2:
                arr.append(v1)
                v1 = None
            else:
                arr.append(v2)
                v2 = None
        if v1 != None:
            arr.append(v1)
            if t1 != None:
                while t1 != None:
                    arr.append(t1.val)
                    t1 = t1.next
        if v2 != None:
            arr.append(v2)
            if t2 != None:
                while t2 != None:
                    arr.append(t2.val)
                    t2 = t2.next
        return to_node(arr)


def to_node(arr):
    if not arr:
        return ListNode(None)
    root = None
    for i in arr[::-1]:
        node = ListNode(i)
        if root:
            node.next = root
        root = node
    return root


arr1 = []
arr2 = [0, 2]
print(to_node(arr1))
node = Solution().mergeTwoLists(to_node(arr1), to_node(arr2))
while node:
    print(node.val)
    node = node.next
