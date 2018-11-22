#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/11/20 20:00
# @File    : 056 Merge Intervals.py
# @Software: PyCharm

"""
Given a collection of intervals, merge all overlapping intervals.

Example 1:
Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:
Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considerred overlapping.
"""


class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    @classmethod
    def create_intervals(cls, list):
        return [cls(*item) for item in list]

    def __repr__(self):
        return '<%r, %r>' % (self.start, self.end)


class Solution(object):
    def merge(self, intervals):
        """
        多个区间中重叠的区间进行合并
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key=lambda x: (x.start, x.end))
        while True:
            flag = False
            for i in range(len(intervals)-2, -1, -1):
                if intervals[i+1].start <= intervals[i].end:
                    intervals[i].end = max(intervals[i].end, intervals[i+1].end)
                    intervals.pop(i+1)
                    flag = True
            if not flag:
                break
        return intervals

    def merge2(self, intervals):
        """
        多个区间中重叠的区间进行合并
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        intervals = sorted(intervals, key=lambda x: x.start)
        res = [intervals[0]]
        for x in intervals[1:]:
            if x.start <= res[-1].end:
                res[-1].end = max(res[-1].end, x.end)
            else:
                res.append(x)
        return res


if __name__ == '__main__':
    intervals = Interval.create_intervals([])
    res = Solution().merge2(intervals)
    print(res)
