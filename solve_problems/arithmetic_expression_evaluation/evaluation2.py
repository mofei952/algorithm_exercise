#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/11/26 19:41
# @File    : evaluation2.py
# @Software: PyCharm

"""
算术表达式求值

1. 中缀表达式建立二叉树
2. 表达式二叉树计算结果
"""

# https://blog.csdn.net/mhxy199288/article/details/38025319
# https://www.jianshu.com/p/6217a257bad2

import re


def _build_tree_string(root, curr_index, index=False, delimiter='-'):
    if root is None:
        return [], 0, 0, 0

    line1 = []
    line2 = []
    if index:
        node_repr = '{}{}{}'.format(curr_index, delimiter, root.value)
    else:
        node_repr = str(root.value)

    new_root_width = gap_size = len(node_repr)

    # Get the left and right sub-boxes, their widths, and root repr positions
    l_box, l_box_width, l_root_start, l_root_end = \
        _build_tree_string(root.left, 2 * curr_index + 1, index, delimiter)
    r_box, r_box_width, r_root_start, r_root_end = \
        _build_tree_string(root.right, 2 * curr_index + 2, index, delimiter)

    # Draw the branch connecting the current root node to the left sub-box
    # Pad the line with whitespaces where necessary
    if l_box_width > 0:
        l_root = (l_root_start + l_root_end) // 2 + 1
        line1.append(' ' * (l_root + 1))
        line1.append('_' * (l_box_width - l_root))
        line2.append(' ' * l_root + '/')
        line2.append(' ' * (l_box_width - l_root))
        new_root_start = l_box_width + 1
        gap_size += 1
    else:
        new_root_start = 0

    # Draw the representation of the current root node
    line1.append(node_repr)
    line2.append(' ' * new_root_width)

    # Draw the branch connecting the current root node to the right sub-box
    # Pad the line with whitespaces where necessary
    if r_box_width > 0:
        r_root = (r_root_start + r_root_end) // 2
        line1.append('_' * r_root)
        line1.append(' ' * (r_box_width - r_root + 1))
        line2.append(' ' * r_root + '\\')
        line2.append(' ' * (r_box_width - r_root))
        gap_size += 1
    new_root_end = new_root_start + new_root_width - 1

    # Combine the left and right sub-boxes with the branches drawn above
    gap = ' ' * gap_size
    new_box = [''.join(line1), ''.join(line2)]
    for i in range(max(len(l_box), len(r_box))):
        l_line = l_box[i] if i < len(l_box) else ' ' * l_box_width
        r_line = r_box[i] if i < len(r_box) else ' ' * r_box_width
        new_box.append(l_line + gap + r_line)

    # Return the new box, its width and its root repr positions
    return new_box, len(new_box[0]), new_root_start, new_root_end


class Node():
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        lines = _build_tree_string(self, 0, False, '-')[0]
        return '\n' + '\n'.join((line.rstrip() for line in lines))


def infix_to_binary_tree(infix, start, end):
    """中缀表达式转二叉树"""
    if re.search('^-?\d+(\.\d+)?$', infix[start:end]):
        return Node(float(infix[start:end]))

    p1 = p2 = -1
    for i in range(start, end):
        x = infix[i]
        if x in ['+', '-']:
            p1 = i
        elif x in ['*', '/']:
            p2 = i
    p = p1 if p1 != -1 else p2

    node = Node(infix[p])
    node.left = infix_to_binary_tree(infix, start, p)
    node.right = infix_to_binary_tree(infix, p + 1, end)
    return node


def binary_tree_evaluation(node):
    """二叉树求值"""
    if node.value not in ['+', '-', '*', '/']:
        return float(node.value)
    v1 = binary_tree_evaluation(node.left)
    v2 = binary_tree_evaluation(node.right)
    if node.value == '+':
        return v1 + v2
    elif node.value == '-':
        return v1 - v2
    elif node.value == '*':
        return v1 * v2
    else:
        return v1 / v2


if __name__ == '__main__':
    s = "-11.2+22*3+44.1"
    # s= "14+23*31*411+522*60+72/6-45+13*12"
    # s = '23-20+2*(1+2*3-5)/4-2*3+3'

    node = infix_to_binary_tree(s, 0, len(s))
    print('二叉树：', node)

    result = binary_tree_evaluation(node)
    print('结果：', result)
