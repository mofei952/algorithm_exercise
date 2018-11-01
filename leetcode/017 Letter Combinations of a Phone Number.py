#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/10/31 19:59
# @File    : 017 Letter Combinations of a Phone Number.py
# @Software: PyCharm

"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example:
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""
from functools import reduce

from utils import print_time


class Solution:
    @print_time
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        letters = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        letter = [letters[int(d) - 2] for d in digits]
        lens = [len(v) for v in letter]
        indexs = [0] * len(letter)
        res = []
        for i in range(reduce(lambda a, b: a * b, lens)):
            comb = ''.join(letter[j][indexs[j]] for j in range(len(letter)))
            res.append(comb)
            indexs[-1] += 1
            if indexs[-1] >= lens[-1]:
                t = len(indexs) - 1
                while t >= 0 and indexs[t] >= lens[t]:
                    indexs[t] = 0
                    indexs[t - 1] += 1
                    t -= 1
        return res

    @print_time
    def letterCombinations2(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        res = ['']
        letters = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        for digit in digits:
            letter = letters[int(digit) - 2]
            res = [s + c for s in res for c in letter]
        return res


if __name__ == '__main__':
    res = Solution().letterCombinations('234569')
    res = Solution().letterCombinations2('234569')
    print(res)
