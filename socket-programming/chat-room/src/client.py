import threading
import socket 

# TO-DO
# - Connect to the chat server 
# - Receive Message from server
# - Send Message to the server


class ChatClient:
    def __init__(self, alias, host='localhost', port=8090):
        self.host = host
        self.port = port
        self.alias = alias 
        self.client_socket = None
    
    def start_client(self):
        """Start the chat client and connect to the server."""

        # Create client socket and connect to the server  
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.host, self.port))

        # Start a thread to listen for incoming messages from the server
        receive_thread = threading.Thread(target=self.receive_messages, args=tuple())
        receive_thread.start()

        # Start a thread to send messages to the server
        send_thread = threading.Thread(target=self.send_messages, args=tuple())
        send_thread.start()

    def receive_messages(self): 
        """Listen for incoming messages from the server and print them"""

        while True:
            try:
                message = self.client_socket.recv(1024)
                message = message.decode('utf-8')

                if message == 'ALIAS?':
                    self.client_socket.sendall(self.alias.encode('utf-8'))
                else:
                    print(message)
                    print()

            except Exception as e:
                print(f"Error occured!")
                self.client_socket.close()
                break

    def send_messages(self): 
        """Send a message to the server."""

        while True: 
            message = input()
            message = f"{self.alias}: {message}"

            try:
                self.client_socket.sendall(message.encode('utf-8'))

            except Exception as e:
                print(f"Error sending message: {e}")


if __name__ == "__main__":
    alias = input("Choose an alias >>> ")
    HOST = '127.0.0.1'
    PORT = 8090

    client = ChatClient(alias, HOST, PORT)
    client.start_client()