import socket
import threading

port = 8090
host = '127.0.0.1'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((host, port))
server.listen()

clients = []
aliases = []

def broadcast(message):
    for client in clients: 
        client.send(message)

def handle_client(client):
    while True: 
        try: 
            message = client.recv(1024)
            broadcast(message)

        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()

            alias = aliases[index]
            broadcast(f"{alias} has left the chat room".encode())
            aliases.remove(alias)
            break

def receive():
    print("Server is running and listening...")

    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        client.send("alias?".encode())
        alias = client.recv(1024).decode()

        aliases.append(alias)
        clients.append(client)

        print(f"The alias of this client is {alias}")
        broadcast(f"{alias} has connected to the chat room".encode())

        client.send("You are now connected to the chat room".encode())

        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

if __name__ == "__main__": 
    receive()









