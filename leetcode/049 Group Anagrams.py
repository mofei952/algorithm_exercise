#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/11/7 18:22
# @File    : 049 Group Anagrams.py
# @Software: PyCharm

"""
Given an array of strings, group anagrams together.

Example:
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

Note:
All inputs will be in lowercase.
The order of your output does not matter.
"""
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs):
        """
        将字符串分类
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashmap = defaultdict(list)
        for s in strs:
            key = [0] * 26
            for c in s:
                key[ord(c) - ord('a')] += 1
            hashmap[tuple(key)].append(s)
        return list(hashmap.values())

    def groupAnagrams2(self, strs):
        """
        将字符串分类
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashmap = defaultdict(list)
        for s in strs:
            key = ''.join(sorted(s))
            hashmap[key].append(s)
        return list(hashmap.values())


if __name__ == '__main__':
    result = Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    print(result)
