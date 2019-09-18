#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 20:57:09 2019
使用match()方法匹配字符串

@author: zhuyangze
"""
import re

print("模式匹配字符串:")
m = re.match('foo', 'foo')
if m is not None:
    print(m.group())
    print(m)

m = re.match('foo', 'bar')
if m is not None:
    print(m.group())

# 模式从字符串的起始部分开始匹配，即使字符串比模式长，匹配也能够成功
m = re.match('foo', 'food on the table')
print(m.group())

# 面向对象的特性
print(re.match('foo', 'food on the table').group())

# match() 与 search()
print("search()查找模式:")
m = re.match('foo', 'seafood')
if m is not None:
    print(m.group())

# search()函数不但会搜索模式在字符串中第一次出现的位置，而且严格地对字符串从左到右搜索
m = re.search('foo', 'seafood')
if m is not None:
    print(m.group())