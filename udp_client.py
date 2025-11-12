import socket

# Server details
server_ip = "127.0.0.1"   # if both on same computer
server_port = 9999
filename = "E:/CN/CNL/codes/udp/test.txt" # the file you want to send

# Create a UDP socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Read file data
with open(filename, "rb") as file:
    data = file.read()

# Send the file to the server
client.sendto(data, (server_ip, server_port))
print("File sent successfully!")

# Close the socket
client.close()
