#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/11/12 20:18
# @File    : 023 Merge k Sorted Lists.py
# @Software: PyCharm

"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:
Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""
import heapq

from utils import ListNode


class Solution:
    def mergeKLists(self, lists):
        """
        合并多个排序好的列表
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return []
        res = lists[0]
        def insert(pre, cur, val):
            nonlocal res
            new_node = ListNode(val)
            if not pre:
                res = new_node
            else:
                pre.next = new_node
            new_node.next = cur
        for i in range(1, len(lists)):
            node = lists[i]
            while node:
                cur = res
                pre = None
                while cur:
                    if cur.val > node.val:
                        insert(pre, cur, node.val)
                        break
                    pre = cur
                    cur = cur.next
                else:
                    insert(pre, None, node.val)
                node = node.next
        return res

    def mergeKLists2(self, lists):
        """
        合并多个排序好的列表，使用heapq
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        ListNode.__lt__ = lambda self, other: self.val < other.val
        heap = []
        for node in lists:
            if node:
                heap.append((node.val, node))
        heapq.heapify(heap)
        head = cur = ListNode(0)
        while heap:
            val, node = heapq.heappop(heap)
            cur.next = node
            cur = cur.next
            if node.next:
                node = node.next
                heapq.heappush(heap, (node.val, node))
        return head.next

    def mergeKLists3(self, lists):
        """
        合并多个排序好的列表
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        node_list = []
        for node in lists:
            while node:
                node_list.append(node)
                node = node.next
        if not node_list:
            return []
        node_list = sorted(node_list, key=lambda x: x.val)
        head = cur = ListNode(0)
        for node in node_list:
            cur.next = node
            cur = node
        return head.next


if __name__ == '__main__':
    input = [
        ListNode.create_linkedlist([0]),
        ListNode.create_linkedlist([1]),
    ]
    result = Solution().mergeKLists3(input)
    print(result)
