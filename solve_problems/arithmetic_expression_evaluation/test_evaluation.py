#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/10/22 21:54
# @File    : test_evaluation.py
# @Software: PyCharm

from solve_problems.arithmetic_expression_evaluation.evaluation2 import evaluation


def test1():
    assert evaluation('1+1') == 2


def test2():
    assert evaluation('1/2') == 0.5


def test3():
    expression = '1234*5678'
    assert evaluation(expression) == eval(expression)


def test4():
    expression = '1.2+2.5'
    assert evaluation(expression) == eval(expression)


def test5():
    expression = '-23+11'
    assert evaluation(expression) == eval(expression)


def test6():
    expression = '2+(2+3*2)*3-5'
    assert evaluation(expression) == eval(expression)


def test7():
    expression = '-23-20+2*(-1+2*-3-5)/-4-2*3+3.6'
    assert evaluation(expression) == eval(expression)


if __name__ == '__main__':
    import pytest

    pytest.main(['test_evaluation.py'])
