# -*- coding: utf-8 -*-
"""
### 作业3:

2. 客户端（Client）类

    实例属性：
        + 服务器端口、服务器地址、socket

    实例方法：
        + start 启动服务器方法（创建socket、链接服务器）
        + recv_file（发送请求、接收文件方法）
"""
import socket

class Client:
    def __init__(self) -> None:
        self.ip = '127.0.0.1'
        self.port = 8000
        self.start()
        self.recv_file()

    def start(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.ip, 8000))

    def recv_file(self):
        server_response = self.socket.recv(1024)
        print(server_response.decode('utf-8'))
        self.socket.send('你好'.encode('utf-8'))

Client()
