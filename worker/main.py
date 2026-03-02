import socket
import time

HOST = "127.0.0.1"
PORT = 5000

def start_worker():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    print("Connected to server")

    while True:
        message = "Hello from worker"
        client_socket.sendall(message.encode())

        data = client_socket.recv(1024)
        print(f"Server says: {data.decode()}")

        time.sleep(3)

if __name__ == "__main__":
    start_worker()