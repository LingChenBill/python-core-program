#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 22:54:25 2019

@author: zhuyangze
"""

import re
f = open('/Users/zhuyangze/Documents/fork/python-core-program/data/whodata.txt', 'r')
for eachline in f:
    # 去除尾部的\n使用str.rstrip()
    print(re.split(r'\s\s+', eachline.rstrip()))
f.close()

import os
f = os.popen('who', 'r')
for eachLine in f:
    print(re.split(r'\s\s+|\t', eachLine.rstrip()))
f.close()