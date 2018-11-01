#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/9/23 14:36
# @File    : test82.py
# @Software: PyCharm


"""
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Example 1:
Input: 1->2->3->3->4->4->5
Output: 1->2->5

Example 2:
Input: 1->1->1->2->3
Output: 2->3
"""


class ListNode(object):
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


class Solution(object):
    def deleteDuplicates(self, head):
        """
        删除重复的节点
        :type head: ListNode
        :rtype: ListNode
        """
        temp = head
        pre = None
        while temp:
            if temp.next and temp.val == temp.next.val:
                t = temp.next
                while t and temp.val == t.val:
                    t = t.next
                temp = t
                if not pre:
                    head = temp
                else:
                    pre.next = temp
            else:
                pre = temp
                temp = temp.next
        return head


if __name__ == '__main__':
    linkedlist = ListNode.create_linkedlist([1, 2, 3, 3, 4, 4, 5])
    result = Solution().deleteDuplicates(linkedlist)
    print(result)
