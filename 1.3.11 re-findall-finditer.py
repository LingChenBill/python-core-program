#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 21:28:09 2019
查找每一次出现的位置

@author: zhuyangze
"""

import re

m = re.findall('car', 'car')
print(m)

m = re.findall('car', 'scary')
print(m)

m = re.findall('car', 'carry the barcardi to the car')
print(m)

print("finditer: ")
s = 'This and that'

m = re.findall(r'(th\w+) and (th\w+)', s, re.I)
print(m)

m = re.finditer(r'(th\w+) and (th\w+)', s, re.I)
print([g.groups() for g in m])

it = re.finditer(r'(th\w+)', s, re.I)
print(it)