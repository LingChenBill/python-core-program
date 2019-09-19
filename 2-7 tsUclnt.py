#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 21:05:02 2019
创建一个UDP客户端，它提示用户输入发送到服务器的消息，
并接收从服务器端返回的添加了时间戳前缀的相同消息，然后将结果展示给用户。

@author: zhuyangze
"""
from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

udpCliSock = socket(AF_INET, SOCK_DGRAM)

while True:
    data = input('> ')
    if not data:
        break
    # 发送一条消息并等待服务器的回复
    udpCliSock.sendto(bytes(data, 'utf-8'), ADDR)

    data, ADDR = udpCliSock.recvfrom(BUFSIZE)

    if not data:
        break
    
    print("data: ", data.decode('utf-8'))

udpCliSock.close()
