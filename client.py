
import socket

host = '127.0.0.1'
port = 12345

# Create a TCP socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((host, port))

# Send data to the server
while True:   
    message = input(">>> ")
    if message == "quit":
        client_socket.close()
    
    client_socket.sendall(message.encode('utf-8'))
    data = client_socket.recv(1024)
    print(f"Received from server: \n{data.decode('utf-8')}")


    