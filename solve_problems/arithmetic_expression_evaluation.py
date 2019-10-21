#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/10/21 21:27
# @File    : arithmetic_expression_evaluation.py
# @Software: PyCharm

from typing import List


def expression_convert(expression: str) -> List:
    """算法表达式字符串转为列表"""
    arr = []
    start = 0
    for i, v in enumerate(expression):
        if not '0' <= v <= '9':
            if i > start:
                arr.append(int(expression[start:i]))
            arr.append(v)
            start = i + 1
    arr.append(int(expression[start:]))
    return arr


def infix2postfix(infix: List) -> List:
    # 中缀表达式转后缀表达式
    postfix = []
    stack = []
    for v in infix:
        if isinstance(v, int):
            postfix.append(v)
        elif v == '(':
            stack.append(v)
        elif v == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()
        elif v in ['+', '-']:
            while stack and stack[-1] in ['*', '/', '+', '-']:
                postfix.append(stack.pop())
            stack.append(v)
        else:
            while stack and stack[-1] in ['*', '/']:
                postfix.append(stack.pop())
            stack.append(v)
    while stack:
        postfix.append(stack.pop())
    return postfix


# 后缀表达式求值
def postfix_evaluation(postfix: List) -> float:
    stack = []
    for v in postfix:
        if isinstance(v, int):
            stack.append(v)
        else:
            op2 = stack.pop()
            op1 = stack.pop()
            if v == '+':
                res = op1 + op2
            elif v == '-':
                res = op1 - op2
            elif v == '*':
                res = op1 * op2
            else:
                res = op1 / op2
            stack.append(res)
    return stack[-1]


if __name__ == '__main__':
    infix = expression_convert('21*(31-5)+7')
    print(infix)
    postfix = infix2postfix(infix)
    print(postfix)
    res = postfix_evaluation(postfix)
    print(res)
