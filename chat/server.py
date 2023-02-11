'''import socket
s =socket.socket()
s.bind(('localhost',6999))

s.listen(3)
print("Server is listening")


c,addr = s.accept()
print('Connected with',addr)
while True:
    cm = c.recv(1024).decode()
    print("Client msg is: ",cm)
    sm = input("Enter server msg: ")
    s.send(bytes(sm,'utf-8'),('localhost',6999))
    print(s.recv(1034).decode())

c.close()

//real code

import socket
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind(("localhost",4999))
data,add=sock.recvfrom(1096)
print(data.decode())
msg="hello client".encode()
sock.sendto(msg,add)
'''

import socket

host = '127.0.0.1'
port = 15000
s = socket.socket()
s.bind((host,port))
s.listen(2)

print("Waiting for clients...")
conn,addr = s.accept()
print("Connected by ", addr)

while True:
    data = conn.recv(1024)
    print('Client Message :' + data.decode())
    if ('quit' in data.decode()) or not data:
        print("Server Exited Successfully!!!")
        conn.close()
        break
    else:
        print('Type your response:',end='')
        st=input()
        conn.sendall(st.encode())
conn.close()