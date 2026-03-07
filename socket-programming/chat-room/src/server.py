import socket 
import threading

# TO-DO
# - Store client connections and its alias in the list
# - Broadcasting message to all clients
# - Handle each client connection in a separate thread 

class ChatServer:
    def __init__(self, host='', port=12345):
        self.host = host
        self.port = port
        self.clients = []
        self.aliases = [] 
        self.server_socket = None
    
    def start_server(self):
        """Start the chat server and listen for incoming connections."""

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)

        print(f"Chat server is running and listening...\n")



        # Listening for incoming connections indefinitely
        while True:
            client_socket, addr = self.server_socket.accept()
            print(f"New connection from {addr}")

            client_socket.send("ALIAS?".encode('utf-8'))

            alias = client_socket.recv(1024).decode('utf-8')

            self.clients.append(client_socket)
            self.aliases.append(alias)

            response = f"{alias} has joined the chat."

            print(response)
            print()

            # broadcast to all clients that a new user has joined
            self.broadcast(response)

            # Spawn a dedicated thread to handle this client's messages
            thread = threading.Thread(target=self.handle_client, args=(client_socket,))
            thread.start()


    def broadcast(self, message):
        """Send a message to all connected clients."""

        for client in self.clients:
            try:
                client.sendall(message.encode('utf-8'))
            except Exception as e:
                print(f"Error sending message to a client: {e}")

    def handle_client(self, client_socket):
        """Handle incoming messages from a client and broadcast them."""
        
        while True: 
            try: 
                message = client_socket.recv(1024).decode('utf-8')

                if not message: 
                    raise Exception("Client disconnected")
                
                self.broadcast(message)

            except: 

                # remove client from list of clients and close the connection
                index = self.clients.index(client_socket)
                self.clients.remove(client_socket)
                client_socket.close()

                alias = self.aliases[index]
                self.aliases.remove(alias)

                # Inform others that this user has left the chat room
                response = f"{alias} has left the chat room."
                print(response)
                print()
                self.broadcast(response)

                break 

    
if __name__ == "__main__": 
    PORT = 8090
    HOST = "127.0.0.1"

    chat_server = ChatServer(HOST, PORT)
    chat_server.start_server()

