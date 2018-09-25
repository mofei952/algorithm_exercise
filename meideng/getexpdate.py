#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/9/25 15:55
# @File    : test1.py
# @Software: PyCharm


def isLeapYear(year):
    return year % 100 != 0 and year % 4 == 0 or year % 400 == 0


def isLegalData(year, month, day):
    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # 若为闰年，2月改为29天
    if isLeapYear(year):
        days[2] = 29
    # year参数不合法
    if year < 0:
        return False
    # month参数不合法
    if month < 1 or month > 12:
        return False
    # day参数不合法
    if day < 1 or day > days[month]:
        return False
    return True

def getExpirationDate(year, month, day):
    # 参数类型错误，必须为int
    if not isinstance(year, int) or not isinstance(month, int) or not isinstance(day, int):
        raise Exception('parameter type is error, must be int')
    # 不合法的日期
    if not isLegalData(year, month, day):
        raise Exception('parameter is illegal')
    # 每个月的天数(平年)
    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # 订购时长为1个月
    add_month = 1
    # 到期年份
    exp_year = year + (month - 1 + add_month) // 12
    # 到期月份
    exp_month = (month - 1 + add_month) % 12 + 1
    # 若到期月份为2月 且 预定日大于28 且 到期年份为闰年，则修改2月份的天数
    if exp_month == 2 and day > 28 and isLeapYear(exp_year):
        days[2] = 29
    # 一般情况下到期日和预定日相同，当到期月的天数小于预定日，取到期月的的最后一天，
    # 即取到期月的天数和预定日中小的值
    exp_day = min(days[exp_month], day)
    return [exp_year, exp_month, exp_day]


# 参数不合法测试
# print(getExpirationDate(1.5, 2, 29)) # parameter type is error, must be int
# print(getExpirationDate(-1, 2, 29))  # parameter is illegal
# print(getExpirationDate(2017, 13, 29))  # parameter is illegal
# print(getExpirationDate(2017, 2, 29))  # parameter is illegal
# 一般情况测试
print(getExpirationDate(2017, 1, 27))  # [2017, 2, 27]
# 到期月天数小于预定日 测试
print(getExpirationDate(2017, 1, 31))  # [2017, 2, 28]  2017年为平年，2月只有28天
print(getExpirationDate(2017, 3, 31))  # [2017, 4, 30]  4月只有30天
print(getExpirationDate(2017, 5, 31))  # [2017, 6, 30]  6月只有30天
print(getExpirationDate(2017, 8, 31))  # [2017, 9, 30]  9月只有30天
print(getExpirationDate(2017, 10, 31))  # [2017, 11, 30]    11月只有30天
# 闰年平年情况测试
print(getExpirationDate(2000, 1, 31))  # [2000, 2, 29]  2000年为闰年，2月有29天
print(getExpirationDate(2020, 1, 31))  # [2020, 2, 29]  2020年为闰年，2月有29天
print(getExpirationDate(2100, 1, 31))  # [2100, 2, 28]  2100年为平年，2月只有28天
# 跨年情况测试
print(getExpirationDate(1999, 12, 31))  # [2000, 1, 31]
