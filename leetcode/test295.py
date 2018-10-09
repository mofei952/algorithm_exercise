#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/10/1 20:48
# @File    : test295.py
# @Software: PyCharm
import heapq


class MedianFinder2(object):
    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num):
        heapq.heappush(self.minHeap, -num)
        heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))
        while len(self.minHeap) < len(self.maxHeap):
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))

    def findMedian(self):
        if len(self.minHeap) == len(self.maxHeap):
            return (self.maxHeap[0] - self.minHeap[0]) / 2
        else:
            return -self.minHeap[0]


class MedianFinder(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if not self.nums:
            self.nums.append(num)
            return
        start = 0
        end = len(self.nums) - 1
        flag = False
        while start <= end:
            mid = (start + end) // 2
            if self.nums[mid] == num:
                flag = True
                self.nums.insert(mid, num)
                break
            elif self.nums[mid] < num:
                start = mid + 1
            else:
                end = mid - 1
        if not flag:
            self.nums.insert(start, num)

    def findMedian(self):
        """
        :rtype: float
        """
        length = len(self.nums)
        if length % 2 == 0:
            return (self.nums[length // 2] + self.nums[length // 2 - 1]) / 2
        else:
            return self.nums[length // 2]


m = MedianFinder2()
a = [1,2,3]
for i in a:
    m.addNum(i)
    print(m.findMedian())
