# Import socket module
import socket

# Create a socket object
s = socket.socket()

# Bind the socket to host and port
s.bind(("0.0.0.0", 9999))

# Listen for incoming connections
s.listen(1)
print("Server ready, waiting for connection...")

# Accept a connection
conn, addr = s.accept()
print("Connected with:", addr)

# Receive message from client
msg = conn.recv(1024).decode()
print("Client says:", msg)

# Send reply to client
conn.send(b"Hello from Server!")

# Close the connection
conn.close()
s.close()