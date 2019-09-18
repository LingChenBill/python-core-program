#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 21:17:45 2019

@author: zhuyangze
"""

import re

print("重复、特殊字符以及分组:")

patt = '\w+@(\w+\.)?\w+\.com'
m = re.match(patt, 'nobody@xx.com')
if m is not None:
    print(m.group())

patt = '\w+@(\w+\.)*\w+\.com'
m = re.match(patt, 'nobody@xx.www.yyy.zzz.com')
if m is not None:
    print(m.group())

print("子组:")
m = re.match('(\w\w\w)-(\d\d\d)', 'abc-123')
print(m.group())
print(m.group(1))
print(m.group(2))
print(m.groups())