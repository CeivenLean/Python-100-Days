#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: xxxl
@file: 2次.py
@datetime: 2020/8/2 3:50 下午
@software: PyCharm
"""


def isPowerOfTwo(n: int) -> bool:
    while n > 1:
        n = n / 2
    return n == 1


print(isPowerOfTwo(n=8))