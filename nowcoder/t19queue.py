#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/10/9 19:36
# @File    : t19queue.py
# @Software: PyCharm

# 用两个栈实现队列
# https://www.nowcoder.com/practice/54275ddae22f475981afa2244dd448c6?tpId=13&tqId=11158&tPage=2&rp=2&ru=/ta/coding-interviews&qru=/ta/coding-interviews/question-ranking


class Solution:
    stack1 = []
    stack2 = []

    def push(self, node):
        self.stack1.append(node)

    def pop(self):
        if self.stack2:
            return self.stack2.pop()
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
