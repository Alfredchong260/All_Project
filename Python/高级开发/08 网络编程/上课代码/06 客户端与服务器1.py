import socket

# 1. 创建一个客户端
tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. 链接服务器
tcp_client_socket.connect(('127.0.0.1', 7788))

# 3. 与服务器交换信息
while True:
    # 3.2 接受服务器发送回来的数据
    recv_data = tcp_client_socket.recv(1024)
    print('接受的数据为：', recv_data.decode('utf-8'))

    # 3.1 发生数据给服务器
    data = input('请输入想要发生给服务器的数据：')
    tcp_client_socket.send(data.encode('utf-8'))


# 4. 关闭与服务器的链接，释放资源
tcp_client_socket.close()
