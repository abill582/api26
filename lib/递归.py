#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2024/5/8 14:26
# AUTHOR    : Yanglei
# @File     : 2024/5/8.py
# @Software : PyCharm
def sum(n):
    if n == 0:
        return 0
    else:
        return n+sum(n-1)

print(sum(5))

def factor(n):
    if n == 0:
        return 1
    else:
        return n*factor(n-1)

print(factor(5))