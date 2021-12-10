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
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.address = (self.host, self.port)
        self.socket = None

    def start(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(self.address)
        self.socket.listen(1024)
        # 客户端的链接,客户端的地址需要绑定到 self 吗 ?
        tcp_client_socket, tcp_client_address = self.socket.accept()
        # 如果有一个新客户链接成功了,调用方法进行处理
        self.handle_recv(tcp_client_socket, tcp_client_address)

    def handle_recv(self, tcp_client_socket, tcp_client_address):
        """处理客户端的请求"""
        self.send_file(tcp_client_socket)

        recv_data = tcp_client_socket.recv(1024)
        print('客户端发送过来的信息:\t', recv_data.decode('utf-8'))

    def send_file(self, tcp_client_socket):
        """发送信息的方法"""
        tcp_client_socket.send('链接服务器成功'.encode('utf-8'))


# 0.0.0.0 开放端口,只要能访问当前电脑的网络,都可以请求
server = Server('0.0.0.0', 7788)
server.start()
