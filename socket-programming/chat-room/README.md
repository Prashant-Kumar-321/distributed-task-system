# Chat Room Application

A simple real-time chat room application built using Python socket programming. This project demonstrates the fundamentals of network programming by allowing multiple clients to connect to a central server and exchange messages in real-time.

## Overview

This chat room application consists of two main components:
- **Server**: A central server that manages client connections, handles message broadcasting, and coordinates communication between clients.
- **Client**: Individual chat clients that connect to the server, send messages, and receive messages from other participants.

The application uses TCP sockets for reliable communication and threading to handle multiple clients concurrently.

## Features

- **Real-time Messaging**: Instant message delivery between connected clients
- **Multi-client Support**: Multiple users can join and chat simultaneously
- **User Aliases**: Each client can set a unique alias for identification
- **Automatic Notifications**: Join/leave notifications when clients connect or disconnect
- **Threaded Architecture**: Server handles multiple clients concurrently without blocking
- **Error Handling**: Graceful handling of client disconnections and network errors
- **Simple Interface**: Command-line based interface for easy testing and demonstration

## Requirements

- Python 3.6 or higher
- Standard library modules: `socket`, `threading`
- No external dependencies required

## Installation

1. Clone or download the project files
2. Ensure Python 3.6+ is installed on your system
3. Navigate to the project directory

```bash
cd /path/to/chat-room
```

## Usage

### Running the Server

1. Open a terminal and navigate to the `src` directory
2. Run the server script:

```bash
python src/server.py
```

The server will start listening on `127.0.0.1:8090` and display connection messages.

### Running the Client

1. Open a new terminal window (keep the server running)
2. Navigate to the `src` directory
3. Run the client script:

```bash
python src/client.py
```

4. Enter your desired alias when prompted
5. Start chatting! Type messages and press Enter to send

### Example Session

**Terminal 1 (Server):**
```
Chat server is running and listening...

New connection from ('127.0.0.1', 54321)
Alice has joined the chat.

New connection from ('127.0.0.1', 54322)
Bob has joined the chat.

Alice: Hello everyone!
Bob: Hi Alice!
Alice has left the chat room.
```

**Terminal 2 (Client - Alice):**
```
Choose an alias >>> Alice
Bob has joined the chat.
Alice: Hello everyone!
Bob: Hi Alice!
```

**Terminal 3 (Client - Bob):**
```
Choose an alias >>> Bob
Alice has joined the chat.
Alice: Hello everyone!
Bob: Hi Alice!
```

## Architecture

### Server Architecture

The server uses a multi-threaded design:

- **Main Thread**: Accepts new client connections and manages the connection lifecycle
- **Client Handler Threads**: One thread per connected client to handle incoming messages
- **Broadcast System**: Centralized message distribution to all connected clients

### Client Architecture

Each client runs two threads:

- **Receive Thread**: Listens for incoming messages from the server
- **Send Thread**: Handles user input and sends messages to the server

### Network Protocol

- **Connection Establishment**: TCP handshake followed by alias exchange
- **Message Format**: UTF-8 encoded strings with alias prefixes
- **Disconnection Handling**: Graceful cleanup when clients disconnect

## Code Structure

```
chat-room/
├── README.md
├── src/
│   ├── server.py      # Main server implementation
│   └── client.py      # Main client implementation
└── tests/
    ├── test_server.py # Server tests
    └── test_client.py  # Client tests
```

### Key Classes

#### ChatServer
- Manages server socket and client connections
- Handles client registration and message broadcasting
- Maintains lists of active clients and their aliases

#### ChatClient
- Manages client socket connection
- Handles message sending and receiving
- Provides user interface for chat interaction

## How It Works

### Server Workflow

1. **Initialization**: Server binds to specified host and port
2. **Connection Acceptance**: Waits for client connections
3. **Alias Request**: Asks new clients for their alias
4. **Registration**: Adds client to active list and broadcasts join message
5. **Message Handling**: Spawns thread to handle client messages
6. **Broadcasting**: Distributes messages to all connected clients
7. **Cleanup**: Removes disconnected clients and broadcasts leave message

### Client Workflow

1. **Connection**: Establishes TCP connection to server
2. **Alias Setup**: Receives alias request and sends chosen alias
3. **Message Threads**: Starts receive and send threads
4. **Receiving**: Continuously listens for server messages
5. **Sending**: Reads user input and sends formatted messages
6. **Disconnection**: Handles graceful disconnection on errors

### Message Flow

```
Client A → Server → Broadcast → ClientA, Client B, Client C, ...
```

## Socket Programming Fundamentals

This application demonstrates core socket programming concepts:

### Server Socket Creation
```python
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(backlog)
```

### Client Socket Creation
```python
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))
```

### Data Transmission
- Messages are encoded to UTF-8 bytes before sending
- Received bytes are decoded back to strings
- Fixed buffer size (1024 bytes) for message chunks

## Troubleshooting

### Common Issues

**Port Already in Use**
- Error: `OSError: [Errno 48] Address already in use`
- Solution: Wait for the port to be released or use a different port

**Connection Refused**
- Error: `ConnectionRefusedError`
- Solution: Ensure the server is running and accessible

**Client Disconnection Issues**
- If clients disconnect abruptly, the server handles cleanup automatically
- Check network connectivity and firewall settings

### Debugging Tips

1. Run server and client in separate terminals
2. Monitor server output for connection status
3. Check for Python version compatibility
4. Verify host and port configurations match

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

### Areas for Improvement

- Add encryption for secure communication
- Implement private messaging
- Add user authentication
- Create a GUI interface
- Add message history/logging


