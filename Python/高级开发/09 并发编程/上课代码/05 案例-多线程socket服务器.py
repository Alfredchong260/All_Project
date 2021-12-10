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
import threading


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
        # 需要同时给多个人提供服务
        while True:  # 循环等待客户的到来
            tcp_client_socket, tcp_client_address = self.socket.accept()
            # 如果有一个新客户链接成功了,调用方法进行处理
            # self.handle_recv(tcp_client_socket, tcp_client_address)
            t1 = threading.Thread(target=self.handle_recv, args=(tcp_client_socket, tcp_client_address))
            t1.start()

    def handle_recv(self, tcp_client_socket, tcp_client_address):
        """处理客户端的请求
            给客户端发送数据 (循环发送)
            接受客户端的数据 (循环接受)
        """

        # self.send_file(tcp_client_socket)
        send_thread = threading.Thread(target=self.send_file, args=(tcp_client_socket,))
        send_thread.start()
        while True:
            recv_data = tcp_client_socket.recv(1024)
            print('收到客户端的信息:\t', recv_data.decode('utf-8'))

            # 服务器发送信息的代码
            tcp_client_socket.send(f'收到了来自:({tcp_client_address}) 的信息'.encode('utf-8'))

    def send_file(self, tcp_client_socket):
        """发送信息的方法"""
        tcp_client_socket.send('链接服务器成功'.encode('utf-8'))


# 0.0.0.0 开放端口,只要能访问当前电脑的网络,都可以请求
server = Server('0.0.0.0', 7788)
server.start()
