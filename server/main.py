import socket

HOST = "127.0.0.1"
PORT = 5000

def start_server():

    # **** Common Pattern Python Networking Code ****

    # Create a TCP/IP server socket which is ready to acccept client connections
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Binding tells the operating system “when a client connects to this address/port, hand me the socket.”

    # ? What do you mean by “hand me the socket”?
    # When a client connects to the server, the operating system creates a new socket for that specific client connection. This new socket is used for communication between the server and that client. By "hand me the socket," we mean that the operating system will give the server the new socket that was created for the client connection, allowing the server to send and receive data with that client.

    server_socket.bind((HOST, PORT))
    
    # Puts the bound socket into listening mode
    server_socket.listen()

    print(f"Server listening on {HOST}:{PORT}")

    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")

    while True:
        data = conn.recv(1024)
        if not data:
            break

        # Converts the received bytes data into a string message
        message = data.decode()
        print(f"Received from worker: {message}")

        # Prepare a response message and send it back to the worker
        response = "Message received"
        encoded_response = response.encode()
        conn.sendall(encoded_response)

    conn.close()

if __name__ == "__main__":
    start_server()