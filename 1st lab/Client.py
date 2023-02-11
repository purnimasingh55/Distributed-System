import socket
c = socket.socket(family = socket.AF_INET , type = socket.SOCK_STREAM)
c.connect(('localhost',1800))
#c.send(bytes("Pass the msg"))
c.recv(10)
c.send(bytes("Pass the msg",'utf-8'))
#x = input("Enter a string")
#c1.send(bytes(x))
c.close()
