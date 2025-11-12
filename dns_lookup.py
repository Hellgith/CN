import socket

data = input("Enter a URL or IP address: ")

# If input looks like an IP address
if data.replace('.', '').isdigit():
    try:
        print("Domain Name:", socket.gethostbyaddr(data)[0])
    except socket.herror:
        print("No domain name found for this IP.")
else:
    try:
        print("IP Address:", socket.gethostbyname(data))
    except socket.gaierror:
        print("Invalid domain name.")