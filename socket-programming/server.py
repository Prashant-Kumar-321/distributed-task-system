# Server socket methods
## bind() - binds the socket to an address and port number
## listen() - listens for incoming connections
## accept() - accepts a connection from a client
## send() - sends data to the client
## recv() - receives data from the client
## close() - closes the socket

import socket 
import sys

if __name__ == "__main__": 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket successfully created")

    port  = 23456

    s.bind(('', port))
    print(f"Socket binded to {port}")

    s.listen(5)
    print("Socket is listening")

    while True: 
        c, addr = s.accept()
        client_ip, client_port = addr
        
        client_message = c.recv(1024)
        print(f"Received message from client: {client_message.decode()}")

        print(f"Got connection from {client_ip} on port {client_port}")

        res_message = "Thank you for connecting"

        c.sendall(res_message.encode())
        c.close()



