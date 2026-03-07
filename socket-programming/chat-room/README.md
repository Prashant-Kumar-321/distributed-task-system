# Socket Programming (Networking Programming)

## Steps to create Server Socket
1. Create a Socket Object
2. Bind the Socket to an Address and Port
3. Listen for Incoming Connections
4. Accept Incoming Connections
5. Handle Client Requests
6. Close the Connection

### code for Server Socket
```python
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP_ADDRESS, PORT))
    server.listen(5)

    while True: 
        client, addr = s.accept()
        client_ip, client_port = addr
        client_message = c.recv(1024)
        res_message = "Thank you for connecting"
        c.sendall(res_message.encode())
        c.close()
```

## Steps to create Client Socket
1. Create a Socket Object
2. Connect to the Server
3. Send and Receive Data
4. Close the Connection

### code for Client Socket
```python
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((IP_ADDRESS, PORT))
    message = "Hello, Server!"
    client.sendall(message.encode())
    response = client.recv(1024)
    print("Received from server:", response.decode())
    client.close()
```


