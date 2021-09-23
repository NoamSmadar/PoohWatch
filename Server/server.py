import socket
import sys
import select
import os

SERVER_ADDRESS = ('127.0.0.1', 8082)


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind(SERVER_ADDRESS)
        server_socket.listen(3)
        connected_clients = []
        client_index = -1
        while client_index < 0 or client_index >= len(connected_clients):
            connected_clients += [server_socket.accept()]
            for i in range(len(connected_clients)):
                print(i, str(connected_clients[i][1]))
            i, o, e = select.select([sys.stdin], [], [], 3)
            if i:
                try:
                    client_index = int(sys.stdin.readline().strip())
                except:
                    pass
            os.system('cls')
        for i in range(len(connected_clients)):
            if i != client_index:
                connected_clients[i][0].close()
        command = input('> ')
        while command != '$exit':
            connected_clients[client_index][0].send(command)
            recv_msg = connected_clients[client_index][0].recv(1024).decode()
            print(recv_msg)
            command = input('> ')


if __name__ == '__main__':
    main()