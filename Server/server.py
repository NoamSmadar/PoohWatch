from select import select as s_select
import socket
import sys
import os

SERVER_ADDRESS = ('127.0.0.1', 8082)


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind(SERVER_ADDRESS)
        server_socket.listen(3)
        print('Listening...')
        client_socket, address = server_socket.accept()
        command = input('> ')
        while command != '$exit':
            if command != '':
                client_socket.send(command.encode())
                recv_msg = client_socket.recv(1024).decode('unicode_escape')
                print(recv_msg)
            command = input('> ')


if __name__ == '__main__':
    main()
