#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/9/25 15:55
# @File    : test1.py
# @Software: PyCharm


def isLeapYear(year):
    """判断参数year的年份是否为闰年"""
    return year % 100 != 0 and year % 4 == 0 or year % 400 == 0


def isLegalData(year, month, day):
    """判断年月日参数日否合法"""
    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # 若为闰年，2月改为29天
    if isLeapYear(year):
        days[2] = 29
    # 参数合法性检查
    return year >= 1 and 1 <= month <= 12 and 1 <= day <= days[month]


def getExpirationDate(year, month, day):
    """根据预定的年月日，返回预定一个月之后到期的时间"""
    # 参数类型错误，必须为int
    if not isinstance(year, int) or not isinstance(month, int) or not isinstance(day, int):
        raise TypeError('getExpirationDate() args must be int')
    # 不合法的日期
    if not isLegalData(year, month, day):
        raise ValueError('getExpirationDate() args is illegal')
    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    add_month = 1  # 订购时长为1个月
    exp_year = year + (month - 1 + add_month) // 12
    exp_month = (month - 1 + add_month) % 12 + 1
    # 若到期月份为2月 且 预定日大于28 且 到期年份为闰年，则修改2月份的天数
    if exp_month == 2 and day > 28 and isLeapYear(exp_year):
        days[2] = 29
    # 一般情况下到期日和预定日相同
    # 当到期月的天数小于预定日，取到期月的的最后一天
    # 即取到期月的天数和预定日中小的值
    exp_day = min(days[exp_month], day)
    return [exp_year, exp_month, exp_day]


def getPeriodTime2(year, month, day):
    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    add_month = 1
    exp_year = year + (month - 1 + add_month) // 12
    exp_month = (month - 1 + add_month) % 12 + 1
    if exp_month == 2 and day > 28 and isLeapYear(exp_year):
        days[2] = 29
    if days[exp_month] < day:
        return days[month] - day + days[exp_month]
    else:
        return days[month]


def getPeriodTime(year, month, day, n):
    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    add_month = n
    exp_year = year + (month - 1 + add_month) // 12
    exp_month = (month - 1 + add_month) % 12 + 1
    if exp_month == 2 and day > 28 and isLeapYear(exp_year):
        days[2] = 29
    sum = 0
    for i in range(month + 1, month + n):
        year2 = year + (i - 1) // 12
        month2 = (i - 1) % 12 + 1
        if month2 == 2:
            if isLeapYear(year2):
                sum += 29
            else:
                sum += 28
        else:
            sum += days[month2]
    if days[exp_month] < day:
        sum += days[month] - day + days[exp_month]
    else:
        sum += days[month]
    return sum


# 参数不合法测试
# print(getExpirationDate(1.5, 2, 29)) # TypeError: getExpirationDate() args must be int
# print(getExpirationDate(-1, 2, 29))  # ValueError: getExpirationDate() args is illegal
# print(getExpirationDate(2017, 13, 29))  # ValueError: getExpirationDate() args is illegal
# print(getExpirationDate(2017, 2, 29))  # ValueError: getExpirationDate() args is illegal
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

print(getPeriodTime(2017, 10, 31, 2))