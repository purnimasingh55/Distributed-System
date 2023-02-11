'''import socket
c = socket.socket()
c.connect(('localhost',6999))

print("Client is connected to server!!! start your chatting")

while True:
    cm = input("Enter the clients msg: ")
    c.sendto(bytes(cm,'utf-8'),('localhost',6999))
    print(c.recv(1024).decode())
    sm = c.recv(1034).decode()
    print("Server msg is: ", sm)




// real code

import socket
csock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
addr=('localhost',4999)
msg="hello server".encode()
csock.sendto(msg,addr)
data,add=csock.recvfrom(1024)
print(data.decode())
    '''



import socket
s = socket.socket()
s.connect(('127.0.0.1',15000))


print("Client is connected to server!!! start your chatting")

while True:
    cm = input("Enter the client msg: ")
    if cm=='quit':
        s.close()
        break
    s.send(cm.encode())
    data = s.recv(1024).decode()
    print('This is the response: ', data)







