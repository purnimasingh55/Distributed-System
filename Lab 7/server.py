from socket import *

server=socket()

server.bind(('localhost',6001))

server.listen()

connection,address=server.accept()

server.send("Enter Size of the Data ".encode())

n=int(server.recv(1024).decode())

server.close()