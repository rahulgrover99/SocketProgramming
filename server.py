import socket
import threading
import time

HOST = "localhost"
PORT = 8081


def connect_to_client(conn, addr):
    print("Connection established")
    data = conn.recv(1024)
    print(f"DATA from Addr: {data}, {addr}")
    time.sleep(10)
    conn.sendall(b"Thanks for interacting with me!")
    conn.close()


print("Starting the server ...")
# s_sock -> Parent socket
s_sock = socket.socket()

s_sock.bind((HOST, PORT))

s_sock.listen()

print(f"Server is listening on {PORT}")

while True:
    # returns a new socket object and the address info
    # new socket object -> child socket
    conn, addr = s_sock.accept()
    t = threading.Thread(target=connect_to_client, args=(conn, addr))
    t.start()
# s_sock.close()
