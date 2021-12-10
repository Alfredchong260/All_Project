"""
    修改 socket 的代码,是socket 服务器能够同时给多个客户端提供服务

        接收到客户端的请求之后，在 files 目录下创建一个 `{客户端地址}.txt` 的文件，用于记录客户端发过来的所有信息
        与客户端进行通信的时候
            + 记录客户端发送的数据到 `{客户端地址}.txt` 文件中，
            + 发送 `你已经有xx条信息记录` 给客户端（信息数量可以从文件中读取）

"""
import socket
import re


class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        self.socket.bind((self.host, self.port))
        self.socket.listen(128)

        # 可以接收到很多个用户的请求
        socket_client, socket_client_addr = self.socket.accept()
        socket_client.send('hellow world!'.encode('utf-8'))
        self.handle_recv(socket_client, socket_client_addr)

    def handle_recv(self, clt_socket, clt_addr):
        """
        :param clt_socket: 客户端的链接
        :param clt_addr: 客户端的地址
        :return:
        """
        print('客户度的ip地址信息', clt_addr)
        while True:
            recv_data = clt_socket.recv(1024)
            filename = recv_data.decode('utf-8')
            length = 0
            try:
                send_data = open(
                    f"./files/{filename}.txt", mode='r', encoding='utf-8').readlines()
                if send_data:
                    clt_socket.send('链接成功'.encode('utf-8'))
                    length = len(send_data)
                    print(send_data)
                    clt_socket.send(f'你已经有{length}条信息记录'.encode('utf-8'))
            except Exception:
                try:
                    filename = re.findall('\d+\.\d+\.\d+\.\d+', filename)
                    if filename:
                        self.create(filename[0])
                        clt_socket.send('已创建新的对话'.encode('utf-8'))
                        self.record(clt_socket, clt_addr[0], length)

                    clt_socket.send('文件格式错误'.encode('utf-8'))

                except Exception:
                    clt_socket.send('请输入文件名'.encode('utf-8'))


    def record(self, clt_socket, clt_addr, index=0):
        while clt_socket:
            recv_data = clt_socket.recv(1024)
            data = recv_data.decode('utf-8')
            print(data)
            if data:
                index += 1
                with open(f'./files/{clt_addr}.txt', 'a', encoding='utf-8') as w:
                    w.write(data + '\n')
                print(f'你已经有{index}条信息记录\n')

    def create(self, filename):
        with open(f"./files/{filename}.txt", 'a', encoding='utf-8') as w:
            w.write('hello world!')


if __name__ == '__main__':
    serve = Server('127.0.0.1', 7788)
    serve.start()
