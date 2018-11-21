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
from utils import ListNode


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
    list = ListNode.create_linked_list([1, 2, 3, 3, 4, 4, 5])
    result = Solution().deleteDuplicates(list)
    print(result)
