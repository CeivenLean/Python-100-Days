#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: xxxl
@file: 正则.py
@datetime: 2020/8/2 2:50 下午
@software: PyCharm
"""
import re


pattern = re.compile(r'hello')
str1 = 'hello world!'
result = pattern.match(str1)
print(result)
