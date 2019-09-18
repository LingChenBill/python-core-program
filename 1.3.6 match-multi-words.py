#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 21:11:09 2019
匹配多个字符串

@author: zhuyangze
"""
import re

print("择一匹配:")
bt = 'bat|bet|bit'
m = re.match(bt, 'bat')
if m is not None:
    print(m.group())

m = re.match(bt, 'blt')
if m is not None:
    print(m.group())

m = re.match(bt, 'He bit me!')
if m is not None:
    print(m.group())

m = re.search(bt, 'He bit me!')
if m is not None:
    print("search: ", m.group())
