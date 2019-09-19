#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 20:49:19 2019
创建一个TCP服务器，它接受来自客户端的消息，
然后将消息加上时间戳前缀并发送回客户端。

@author: zhuyangze
"""
from socket import *
from time import ctime

HOST = ''
PORT = 21568
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
# 将地址绑定到套接字上
tcpSerSock.bind(ADDR)
# 设置并启动TCP监听器
tcpSerSock.listen(5)

while True:
    print("waiting for connection...")
    # 被动接受TCP客户端连接，一直等待直到连接到达
    tcpCliSock, addr = tcpSerSock.accept()
    print("...connected from: ", addr)
    
    while True:
        # 接收TCP消息
        data = tcpCliSock.recv(BUFSIZE)
        if not data:
            break
        
        print(data)
        
        # 加上时间戳
        s = '[%s] %s' % (ctime(), data.decode())
        # 发送TCP消息
        tcpCliSock.send(bytes(s, 'utf-8'))
        
    tcpCliSock.close()

tcpSerSock.close()
