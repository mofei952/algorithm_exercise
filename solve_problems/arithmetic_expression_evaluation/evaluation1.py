#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/10/21 21:27
# @File    : evaluation1.py
# @Software: PyCharm

"""
算术表达式求值方案1

1. 中缀表达式字符串转换为中缀表达式序列
2. 中缀表达式序列转换为后缀表达式序列
3. 后缀表达式计算结果
"""

from typing import List

from solve_problems.arithmetic_expression_evaluation.common import expression_convert


def infix2postfix(infix: List) -> List:
    # 中缀表达式转后缀表达式
    postfix = []
    stack = []
    for c in infix:
        if isinstance(c, (int, float)):
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


def priority(op):
    """运算符优先级"""
    if op in ['+', '-']:
        return 1
    elif op in ['*', '/']:
        return 2
    return -1


def postfix_evaluation(postfix: List) -> float:
    """后缀表达式求值"""
    stack = []
    for c in postfix:
        if isinstance(c, (int, float)):
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


def evaluation(expression):
    """算术表达式求值"""
    infix = expression_convert(expression)
    postfix = infix2postfix(infix)
    res = postfix_evaluation(postfix)
    return res


if __name__ == '__main__':
    expression = '-23-20+2*(-1+2*-3-5)/-4-2*3+3.6'
    print('中缀表达式字符串：', expression)

    infix = expression_convert(expression)
    print('中缀表达式序列：', infix)

    postfix = infix2postfix(infix)
    print('后缀表达式序列：', postfix)

    res = postfix_evaluation(postfix)
    print('结果：', res)
