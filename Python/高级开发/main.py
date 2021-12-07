import socket

'''
socket.AF_INET ipv4
socket.AF_INET6 ipv6

socket.SOCK_STREAM TCP协议
'''

# Client server
tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_client_socket.connect(('127.0.0.1', 8000))

data = input('Please input the data you want to send:')
tcp_client_socket.send(data.encode('utf-8'))

recv_data = tcp_client_socket.recv(1024)
print(recv_data)

tcp_client_socket.close()

