import socket 
import sys 

def server_socket():

    # Create a socket object 
    try:  
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Socket successfully created")

    except socket.error as err: 
        print(f"socket creation failed with error {err}")
    
    port = 80

    # Get the IP address of the host (Github)
    host_name = "www.github.com"
    try: 
        host_ip = socket.gethostbyname(host_name)
        
    except socket.gaierror as err:
        print(f"Error resolving the host")
        sys.exit()
    
    client_socket.connect((host_ip, port))

    print(f"Socket has successfully connected to Github {host_ip} on port {port}")
    




if __name__ == "__main__":
    server_socket()