import socket

# Create a UDP socket
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to all network addresses, port 9999
server.bind(("0.0.0.0", 9999))
print("Server is ready and waiting for a file...")

# Receive data (up to 1 MB)
data, address = server.recvfrom(1000000)

# Save received data into a file
with open("received_file.txt", "wb") as file:
    file.write(data)

print("File received successfully! Saved as 'received_file.txt'")

# Close the connection
server.close()