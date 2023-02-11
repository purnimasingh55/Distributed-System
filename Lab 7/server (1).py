from socket import *
from time import *

server = socket()

server.bind(('localhost', 9001))

server.listen()
print("Up and Running\n")

connection, address = server.accept()
connection.send("Enter Size of the Data :".encode())

n = connection.recv(1024).decode()
n = int(n)
print(n)
connection.send("Enter Size of the Window :".encode())
k = connection.recv(1024).decode()
k = int(k)
print(k)

for i in range(int(n)):
    connection.send(f"Frame Number {i % int(k)}   Data :{i + 1}".encode())
    connection.send(str(i % k).encode())
    print(connection.recv(1024).decode())
    sleep(0.3)

server.close()