#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 22:07:28 2019
在限定模式上使用split()分隔字符串

@author: zhuyangze
"""

import re

print("split: ")

m = re.split(':', 'str1:str2:str3')
print(m)

DATA = (
        'Mountain View, CA 94040',
        'Sunnyvale, CA',
        'Los Altos, 94023',
        'Cupertino 95014',
        'Palo Alto CA'
        )

for datum in DATA:
    print(re.split(', | (?=(?:\d{5}|[A-Z]{2}))', datum))

# (?iLmsux)系列选项，用户可以直接在正则表达式里面指定一个或者多个标记。
print("?iLmsux系列参数: ")
m = re.findall(r'(?i)yes', 'yes? Yes. YES!!')
print(m)

# m:多行混合
print("?im: ")
m = re.findall(r'(?im)(^th[\w ]+)', """
This line is the first,
another line,
that line, it's the end.
""")
print(m)

# re.s/DOTALL: 该标记表明点号能够用来表示\n
print("?s: ")
m = re.findall(r'(?s)th.+', '''
The first line
the second line
the third line
''')
print(m)