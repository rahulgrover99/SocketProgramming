import socket
# Server's address
HOST = "localhost"
PORT = 8081
c_sock = socket.socket()

c_sock.connect((HOST, PORT))

c_sock.sendall(b"Hello, world!")
response = c_sock.recv(1024)

print(response)

c_sock.close()