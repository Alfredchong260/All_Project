import socket

"""
socket.AF_INET  ipv4
socket.AF_INET6  ipv6

socket.SOCK_STREAM  tcp 的协议  （udp 不学）
"""
# 1. 创建一个客户端
tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. 链接服务器
tcp_client_socket.connect(('127.0.0.1', 7788))

# 你一句我一句


# 3. 与服务器交换信息
# 3.1 发生数据给服务器
while True:
    # 在发生信息的同时可以接受数据，
    # 以目前学习的知识，可以同时收发数据么？ （会等待人的操作）
    data = input('请输入想要发生给服务器的数据：')
    tcp_client_socket.send(data.encode('utf-8'))
    # 3.2 接受服务器发送回来的数据 （会等待人的操作）
    recv_data = tcp_client_socket.recv(1024)  # 一次性最大接受1024个字节
    if recv_data.decode('utf-8') == '下次再聊':
        break
    print('接受的数据为：', recv_data.decode('utf-8'))

# 4. 关闭与服务器的链接，释放资源
tcp_client_socket.close()
