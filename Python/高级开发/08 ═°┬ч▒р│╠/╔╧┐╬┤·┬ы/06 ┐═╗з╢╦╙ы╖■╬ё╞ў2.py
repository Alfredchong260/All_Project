import socket

# 1. 创建socket服务器
tcp_socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. 绑定地址与端口
tcp_socket_server.bind(('0.0.0.0', 7788))

# 3. 监听端口
tcp_socket_server.listen(20)
print('服务器已经启动了')

# 4 等待客户端的链接
new_client_socket, client_addr = tcp_socket_server.accept()
print(f'当前的客户：{new_client_socket}, 客户从哪里来：{client_addr}')

# 5. 客户端来链接之后提供服务
new_client_socket.send('欢迎光临正心杂货铺'.encode('utf-8'))

# 服务器不能手动输入数据，只能提前写好逻辑
while True:
    # 5. 客户端来链接之后提供服务
    new_client_socket.send('欢迎光临正心杂货铺'.encode('utf-8'))

    recv_data = new_client_socket.recv(1024)
    print('客户端的信息：', recv_data.decode('utf-8'))
    if recv_data.decode('utf-8') == '结账':
        break
new_client_socket.close()  # 停止服务
tcp_socket_server.close()  # 关闭店铺

"""
    端口占用： 一个端口只能被一个程序使用
    ctrl + alt + .  选择任务管理器
"""