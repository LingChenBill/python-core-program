#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 21:46:21 2019
使用sub()和subn()搜索与替换

@author: zhuyangze
"""

import re

print("sub: ")
m = re.sub('X', 'Mr. Smith', 'attn: X\n\nDear X, \n')
print(m)

print("subn: ")
m = re.subn('X', 'Mr. Smith', 'attn: X\n\nDear X, \n')
print(m)

m = re.sub('[ae]', 'X', 'abcdef')
print(m)

m = re.subn('[ae]', 'X', 'abcdef')
print(m)

print("日期格式替换:")
m = re.sub(r'(\d{1,2})/(\d{1,2})/(\d{2}|\d{4})', r'\2/\1/\3', '2/20/91')
print(m)

m = re.sub(r'(\d{1,2})/(\d{1,2})/(\d{2}|\d{4})', r'\2/\1/\3', '2/20/1991')
print(m)