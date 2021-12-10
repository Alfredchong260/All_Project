"""

    服务器: 腾讯云服务器(硬件) / 开发一个 app 的服务器(软件) / 只要是提供服务的就是服务器(软件硬件都可以)

socket 是基于 C/S 架构的，也就是说进行 socket 网络编程，通常需要编写两个 py 文件，一个服务端，一个客户端。

client/server  客户端（手机应用、电脑应用、需要服务器提供服务的应用） 服务器

b/server  浏览器 （浏览器） 服务器

服务器（提供服务）	 web服务器（专门返回网页） 	腾讯云服务器（部署写好的服务程序 物理设备）
"""
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
data = input('请输入想要发生给服务器的数据：')
tcp_client_socket.send(data.encode('utf-8'))
# 3.2 接受服务器发送回来的数据
recv_data = tcp_client_socket.recv(1024)  # 一次性最大接受1024个字节
print('接受的数据为：', recv_data.decode('utf-8'))

# 4. 关闭与服务器的链接，释放资源
tcp_client_socket.close()

"""
    编码一定要一致
    bit byte kb mb gb tb 
    
    
    服务器必须绑定地址与端口
    127.0.0.1 本地回环地址，只有本地服务器才能访问
    0.0.0.0   开放地址，任意可以当问到当前电脑的ip都可以访问
    192.168.0.53   只有 192.168.0.x 的电脑才能访问
"""