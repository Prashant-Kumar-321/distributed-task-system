import socket 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket successfully created")

port = 23456
ip = '127.0.0.1'

s.connect((ip, port))

message = "Hello, Server!"
s.sendall(message.encode())

response = s.recv(1024)
print(f"Received from server: {response.decode()}")

s.close()


