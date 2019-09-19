#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 22:44:24 2019
创建一个时间戳客户端，如何与类似文件的SocketServer类StreamRequest Handler对象通信。

@author: zhuyangze
"""
from socket import *

HOST = 'localhost'
PORT = 21569
BUFSIZE = 1024
ADDR = (HOST, PORT)

while True:
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    data = input('> ')
    if not data:
        break
    
    tcpCliSock.send(bytes('%s\r\n' % data, 'utf-8'))
    data = tcpCliSock.recv(BUFSIZE)
    if not data:
        break
    print("data: ", data.decode('utf-8').strip())
tcpCliSock.close()
