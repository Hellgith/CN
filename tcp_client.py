# Import socket module
import socket

# Create a socket object
s = socket.socket()

# Connect to the server
ip = input("Enter server IP (e.g., 127.0.0.1): ")
s.connect((ip, 9999))

# Send a message to the server
s.send(b"Hello from Client!")

# Receive and print message from server
msg = s.recv(1024).decode()
print("Server says:", msg)

# Close the connection
s.close()