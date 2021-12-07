import socket

# Browser server
tcp_server_scoket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_server_scoket.bind(('127.0.0.1', 7788))

tcp_server_scoket.listen(20)
print('服务器已启动')

new_client_socket, client_addr = tcp_server_scoket.accept()
print(f"当前客户：{ new_client_socket }, 客户地址：{ client_addr }")


new_client_socket.send('欢迎光临'.encode('utf-8'))
recv_data = new_client_socket.recv(1024)
print(recv_data.decode('utf-8'))

new_client_socket.close()
tcp_server_scoket.close()
