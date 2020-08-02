#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: xxxl
@file: 数字相关.py
@datetime: 2020/8/2 3:18 下午
@software: PyCharm
"""
'''
数字反转
'''
num = int(input('num = '))
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    # print(reversed_num)
    num //= 10
print(reversed_num)