import sys
import socket
import threading

def server_loop(local_host, local_port, remote_host, remote_port, receive_first):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind((local_host, local_port))
    except:
        print("[!!] Failed to listen on %s:%d" % (local_host, local_host))
        print("[!!] Check for other listening sockets or correct permissions")
        sys.exit()

    print("[*] Listening on %s:%d" % (local_host, local_port))

    server.listen(5)

    while True:
        client_socket, addr = server.accept()
        print("[==>] Received incoming connection from %s:%d" % (addr[0], addr[1]))
        proxy_thread = threading.Thread(target=proxy_handler, args=(client_socket, remote_host, remote_port, receive_first))
        proxy_thread.start()

def proxy_handler(client_socket, remote_host, remote_port, receive_first):
    remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    remote_socket.connect((remote_host, remote_port))

    if receive_first:
        remote_buffer = receive_form(remote_socket)
        hexdump(remote_buffer)

        if len(remote_buffer):
            print('[<==] Sending %d bytes to localhost' % len(remote_buffer))
            client_socket.send(remote_buffer)

        while True:
            local_buffer = receive_form(client_socket)
            if len(local_buffer):
                print('[==>] Received %d bytes from localhost' % len(local_buffer))
                hexdump(local_buffer)
                local_buffer = request_handler(local_buffer)

                remote_socket.send(local_buffer)
                print('[==>] Sent to remote')

            remote_buffer = receive_form(remote_socket)

def main():
    if len(sys.argv[1:]) != 5:
        print("Usage: python3 2.py [localhost] [localport] [remotehost] [remoteport] [receive_first]")
        print("Example: python3 2.py 127.0.0.1 9000 10.12.132.1 9000 True")
        sys.exit()

    local_host = sys.argv[1]
    local_port = int(sys.argv[2])
    remote_host = sys.argv[3]
    remote_port = int(sys.argv[4])
    receive_first = sys.argv[5]

    if "True" in receive_first:
        receive_first = True
    else:
        receive_first = False

    server_loop(local_host, local_port, remote_host, remote_port, receive_first)

main()
