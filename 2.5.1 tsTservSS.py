#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 22:36:29 2019
通过使用socketserver类，TCPServer和StreamRequestHandler,
创建一个时间戳TCP服务器

socketserver请求处理程序的默认行为是接受连接、获取请求，然后关闭连接。
@author: zhuyangze
"""

from socketserver import (TCPServer as TCP, StreamRequestHandler as SRH)
from time import ctime

HOST = ''
PORT = 21569
ADDR = (HOST, PORT)

# 请求处理程序
class MyRequestHandler(SRH):
    def handle(self):
        print("...Connected from: ", self.client_address)
        
        # 使用readline()来获取客户端消息
        s = '[%s] %s' % (ctime(), self.rfile.readline().decode())
        
        # 利用write()将字符串发送回客户端
        self.wfile.write(bytes(s, 'utf-8'))

tcpServ = TCP(ADDR, MyRequestHandler)
print("waiting for connection...")
tcpServ.serve_forever()