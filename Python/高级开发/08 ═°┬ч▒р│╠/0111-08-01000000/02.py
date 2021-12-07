# -*- coding: utf-8 -*-
"""
### 作业2:

将tcp文件下载案例中的代码，用面向对象思想进行封装。

1. 服务器（Server）类
    实例属性：
        + 端口、地址、socket

    实例方法：
        - start 启动服务器方法（创建socket、绑定端口、提供服务）
        - handle_recv 处理客户端请求
        - send_file（发送文件方法）

实现两个对象的通信
"""
import socket

class Server:
    def __init__(self):
        self.ip = '127.0.0.1'
        self.port = 8000
        print('服务器开始服务')
        self.start()
        self.send_file()
        self.handle_recv()
        # self.socket.close()

    def start(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.ip, self.port))

    def handle_recv(self):
        self.socket.listen(20)
        self.client, self.ip = self.socket.accept()
        self.recv_data = self.client.recv(1024)
        print(self.recv_data.decode('utf-8'))

    def send_file(self):
        info = f'成功链接服务器'
        self.client.send(info.encode('utf-8'))

Server()
