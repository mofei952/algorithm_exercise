#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/9/23 14:36
# @File    : test82.py
# @Software: PyCharm

# 删除链表中重复的结点
# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp = head
        pre = None
        while temp is not None:
            if temp.next and temp.val == temp.next.val:
                t = temp.next
                while t and temp.val == t.val:
                    temp.next = t.next
                    t = t.next
                if not pre:
                    head = temp.next
                    temp = head
                else:
                    pre.next = temp.next
                    temp = pre.next
            else:
                pre = temp
                temp = temp.next

        return head


def create_linkedlist(nums):
    link = ListNode(nums[0])
    temp = link
    for i in nums[1:]:
        temp.next = ListNode(i)
        temp = temp.next
    return link


link = create_linkedlist([1, 1])
link = Solution().deleteDuplicates(link)
print(link)
