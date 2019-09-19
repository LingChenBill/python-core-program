#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 20:49:19 2019
创建一个UDP服务器，它接受来自客户端的消息，
然后将消息加上时间戳前缀并发送回客户端。

@author: zhuyangze
"""
from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

udpSerSock = socket(AF_INET, SOCK_DGRAM)
# 将地址绑定到套接字上
udpSerSock.bind(ADDR)

while True:
    print("waiting for message...")
    # 被动接受客户端消息
    data, addr = udpSerSock.recvfrom(BUFSIZE)
    
    # 加上时间戳
    s = '[%s] %s' % (ctime(), data.decode())
    udpSerSock.sendto(bytes(s, 'utf-8'), addr)
    
    print("...received from and returned to: ", addr)

udpSerSock.close()

