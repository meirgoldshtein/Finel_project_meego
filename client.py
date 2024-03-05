
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
    
    client_socket.send(message.encode('utf-8'))
    while True:   
        data = client_socket.recv(4096)
        print(f"{data.decode('utf-8')}")
        if "$finish$" in data.decode('utf-8'):
            break
        


    