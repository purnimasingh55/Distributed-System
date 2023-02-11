import socket
c = socket.socket(family = socket.AF_INET , type = socket.SOCK_STREAM)
c.connect(('localhost',1800))
c.send(bytes("Pass the msg".encode()))
c.recv(10)


