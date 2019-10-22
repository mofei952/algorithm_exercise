#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/10/21 21:27
# @File    : arithmetic_expression_evaluation.py
# @Software: PyCharm

from typing import List


def priority(op):
    """运算符优先级"""
    if op in ['+', '-']:
        return 1
    elif op in ['*', '/']:
        return 2
    return -1


def expression_convert(expression: str) -> List:
    """算术表达式字符串转为列表"""
    arr = []
    flag = False  # 标记前一个元素是否为数字
    for i, c in enumerate(expression):
        if '0' <= c <= '9':
            if flag:
                arr[-1] = arr[-1] * 10 + int(c)
            else:
                arr.append(int(c))
            flag = True
        else:
            arr.append(c)
            flag = False
    return arr


def infix2postfix(infix: List) -> List:
    # 中缀表达式转后缀表达式
    postfix = []
    stack = []
    for c in infix:
        if isinstance(c, int):
            postfix.append(c)
        elif c == '(':
            stack.append(c)
        elif c == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()
        else:
            while stack and priority(stack[-1]) >= priority(c):
                postfix.append(stack.pop())
            stack.append(c)
    while stack:
        postfix.append(stack.pop())
    return postfix


# 后缀表达式求值
def postfix_evaluation(postfix: List) -> float:
    stack = []
    for c in postfix:
        if isinstance(c, int):
            stack.append(c)
        else:
            op2 = stack.pop()
            op1 = stack.pop()
            if c == '+':
                res = op1 + op2
            elif c == '-':
                res = op1 - op2
            elif c == '*':
                res = op1 * op2
            else:
                res = op1 / op2
            stack.append(res)
    return stack[-1]


if __name__ == '__main__':
    expression = '23-20+2*(1+2*3-5)/4-2*3+3'
    print('中缀表达式字符串：', expression)

    infix = expression_convert(expression)
    print('中缀表达式序列：', infix)

    postfix = infix2postfix(infix)
    print('后缀表达式序列：', postfix)

    res = postfix_evaluation(postfix)
    print('结果：', res)
