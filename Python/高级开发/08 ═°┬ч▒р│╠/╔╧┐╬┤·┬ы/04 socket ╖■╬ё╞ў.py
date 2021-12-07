import socket

# 1. 创建socket服务器
tcp_socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. 绑定地址与端口
# 127.0.0.1, 7788
# 192.168.0.53, 7788
# 0.0.0.0, 7788
tcp_socket_server.bind(('0.0.0.0', 7788))

# 3. 监听端口
tcp_socket_server.listen(20)  # 最多同时二十个人进行访问
print('服务器已经启动了')
# 4. 等待客户段的链接
new_client_socket, client_addr = tcp_socket_server.accept()
print(f'当前的客户：{new_client_socket}, 客户从哪里来：{client_addr}')

# 5. 客户端来链接之后提供服务
new_client_socket.send('欢迎光临正心杂货铺'.encode('utf-8'))
recv_data = new_client_socket.recv(1024)
print('客户端的信息：', recv_data.decode('utf-8'))

new_client_socket.close()  # 停止服务
tcp_socket_server.close()  # 关闭店铺
