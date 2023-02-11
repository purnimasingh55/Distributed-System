import socket
from threading import Thread

def receive():
    while True:
        data = c.recv(10).decode("utf8")
        print(data)


host = 'localhost'
port = 12345
addr = (host,port)
c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c.connect(addr)
print("enter your name")
name = input()
c.send(bytes(name,"utf8"))
Thread(target = receive).start()
while True:
    #print(name,end = '')
    data = input()
    c.send(bytes(data,'utf8'))
