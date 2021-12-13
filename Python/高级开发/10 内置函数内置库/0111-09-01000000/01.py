"""
    修改 socket 的代码,是socket 服务器能够同时给多个客户端提供服务

        接收到客户端的请求之后，在 files 目录下创建一个 `{客户端地址}.txt` 的文件，用于记录客户端发过来的所有信息
        与客户端进行通信的时候
            + 记录客户端发送的数据到 `{客户端地址}.txt` 文件中，
            + 发送 `你已经有xx条信息记录` 给客户端（信息数量可以从文件中读取）
"""
import socket
import threading


class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        self.socket.bind((self.host, self.port))
        self.socket.listen(128)

        # 可以接收到很多个用户的请求
        print('服务器已经启动')
        while True:
            socket_client, socket_client_addr = self.socket.accept()
            # self.handle_recv(socket_client, socket_client_addr)
            print('客户端链接成功')
            t1 = threading.Thread(target=self.handle_recv, args=(socket_client, socket_client_addr))
            t1.start()

    def handle_recv(self, clt_socket, clt_addr):
        """
        :param clt_socket: 客户端的链接
        :param clt_addr: 客户端的地址
        :return:
        """
        print('客户度的ip地址信息', clt_addr)
        filename = clt_addr[0] + '-' + str(clt_addr[1]) + '.txt'
        while True:
            # ('127.0.0.1', 4561)
            recv_data = clt_socket.recv(1024)
            print('接受到的数据:\t', recv_data.decode())
            open('files\\' + filename, mode='a', encoding='utf-8').write(recv_data.decode() + '\n')

            # 直接发送 hello world ! 回去
            # hello world ！ 能不能从本地文件里面读取出来 ？
            # 文件的名字能不能让客户端传递过来 ？
            liens = open('files\\' + filename, mode='r', encoding='utf-8').readlines()
            clt_socket.send(f'你已经有{len(liens)}条信息记录'.encode('utf-8'))
            # 如果需要传递的是一张图片/一个程序/或者一个word文档?


if __name__ == '__main__':
    # 逻辑代码是下载 if __name__ == '__main__':
    serve = Server('127.0.0.1', 7788)
    serve.start()
