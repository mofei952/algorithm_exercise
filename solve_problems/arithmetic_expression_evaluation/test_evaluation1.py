#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/10/22 21:54
# @File    : test_evaluation.py
# @Software: PyCharm

from solve_problems.arithmetic_expression_evaluation.evaluation1 import evaluation


def test1():
    assert evaluation('1+1') == 2


def test2():
    assert evaluation('1/2') == 0.5


def test3():
    assert evaluation('1234*5678') == 1234 * 5678


def test4():
    assert evaluation('1.2+2.5') == 1.2 + 2.5


def test5():
    assert evaluation('2+(2+3*2)*3-5') == 2 + (2 + 3 * 2) * 3 - 5


def test6():
    assert evaluation('23-20+2*(1+2*3-5)/4-2*3+3.6') == 23 - 20 + 2 * (1 + 2 * 3 - 5) / 4 - 2 * 3 + 3.6


if __name__ == '__main__':
    import pytest

    pytest.main(['test_evaluation1.py'])
