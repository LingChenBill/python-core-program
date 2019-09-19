#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 21:05:02 2019
创建一个TCP客户端，它提示用户输入发送到服务器的消息，
并接收从服务器端返回的添加了时间戳前缀的相同消息，然后将结果展示给用户。

@author: zhuyangze
"""
from socket import *

HOST = 'localhost'
PORT = 21568
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
# 主动发起TCP服务器连接
tcpCliSock.connect(ADDR)

while True:
    data = input('> ')
    if not data:
        break
    tcpCliSock.send(bytes(data, 'utf-8'))

    # 接收TCP消息
    data = tcpCliSock.recv(BUFSIZE)
    if not data:
        break
    
    print("data: ", data.decode('utf-8'))

tcpCliSock.close()
