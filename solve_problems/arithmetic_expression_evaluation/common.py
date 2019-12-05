#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/12/5 17:26
# @File    : common.py
# @Software: PyCharm

import re
from typing import List


def expression_convert(expression: str) -> List:
    """算术表达式字符串转为列表"""

    strs = re.split(r'([\+\*\/\(\)]|(?<=[\d\)])\-)', expression)
    strs = list(filter(None, strs))  # 去除值为假的元素

    # 验证格式正确性 number转换为对应类型
    for i, s in enumerate(strs):
        if s in ['(', ')', '+', '-', '*', '/']:
            continue
        assert re.search(r'^-?\d+(\.\d+)?$', s), 'illegal number: {}'.format(i)
        converter = float if '.' in s else int
        strs[i] = converter(s)

    return strs