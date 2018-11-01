#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/10/30 11:10
# @File    : test.py
# @Software: PyCharm


"""
1. 数据结构转换

已知一个思维导图对应的文件存储格式如下（邮件附件提供[history.csv](history.csv)）：

```
奴隶社会,非洲,古埃及文明,金字塔
,亚洲,两河流域文明,汉谟拉比法典
,,古印度,种姓制度
,,,佛教的创立
,欧洲,希腊,希腊城邦
,,,雅典民主
,,罗马,城邦
,,,帝国的征服与扩展
,,希腊罗马古典文化,建筑艺术
,,,公历
```


##### 考题1: 将上述数据按照如下规则转换成与思维导图结构相同的json

示例：
```
奴隶社会,非洲
,亚洲
,,古印度
,欧洲
```

转换成的json如下：
```
{
    "奴隶社会":[{
            "非洲":[]
        },{
            "亚洲":[{
                "古印度":[]
            }]
        },{
            "欧洲":[]
        }]
    }]
}
```
##### 考题2: 以上题转换的结果为基础，实现一个key search 方法。
要求：
1. 提交思维导图格式转换json的源代码
1. 提交实现关键词搜索的源代码

"""
import json
import re


def convert(text):
    strs = re.split('\n', text)
    result = {}
    dict = {}
    for str in strs:
        r = re.search('[^,]', str)
        level = r.start()
        s_list = str[level:].split(',')
        if level == 0:
            dict[level] = result[s_list[0]] = []
            level += 1
            s_list = s_list[1:]
        for s in s_list:
            dict[level] = []
            dict[level - 1].append({s: dict[level]})
            level += 1
    return json.dumps(result)


def search(data, key):
    data = json.loads(data)
    queue = [(k, v) for k, v in data.items()]
    result = []
    while queue:
        kv = queue.pop(0)
        if key in kv[0]:
            result.append(kv[0])
        for d in kv[1]:
            for k, v in d.items():
                queue.append((k, v))
    return result


def dfs_print(data, level=0):
    if isinstance(data, str):
        data = json.loads(data)
    if isinstance(data, list):
        for d in data:
            dfs_print(d, level)
    elif isinstance(data, dict):
        for k, v in data.items():
            print('-' * level + k)
            dfs_print(v, level + 1)


if __name__ == '__main__':
    with open('history.csv', 'r', encoding='utf8') as f:
        text = f.read()
    json_str = convert(text)
    dfs_print(json_str)
    # json_str结构如下
    # {
    #     '奴隶社会': [{
    #         '非洲': [{
    #             '古埃及文明': [{
    #                 '金字塔': []
    #             }]
    #         }]
    #     }, {
    #         '亚洲': [{
    #             '两河流域文明': [{
    #                 '汉谟拉比法典': []
    #             }]
    #         }, {
    #             '古印度': [{
    #                 '种姓制度': []
    #             }, {
    #                 '佛教的创立': []
    #             }]
    #         }]
    #     }, {
    #         '欧洲': [{
    #             '希腊': [{
    #                 '希腊城邦': []
    #             }, {
    #                 '雅典民主': []
    #             }]
    #         }, {
    #             '罗马': [{
    #                 '城邦': []
    #             }, {
    #                 '帝国的征服与扩展': []
    #             }]
    #         }, {
    #             '希腊罗马古典文化': [{
    #                 '建筑艺术': []
    #             }, {
    #                 '公历': []
    #             }]
    #         }]
    #     }]
    # }
    print(search(json_str, '希腊'))  # ['希腊', '希腊罗马古典文化', '希腊城邦']
    print(search(json_str, '洲'))  # ['非洲', '亚洲', '欧洲']
