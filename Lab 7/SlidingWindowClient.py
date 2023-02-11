import socket

c=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostname()
port=9809
c.connect((host,port))
c.send(bytes('Client successfully connected to server!!! Ready to send the acknowledgement','utf-8'))

print(c.recv(1024).decode())
n = int(input())
n = str(n)

c.send(n.encode())
print(c.recv(1024).decode())

m = int(input())
m = str(m)

c.send(m.encode())
for i in range(int(n)):
    print(c.recv(1024).decode())
    ack = c.recv(1024).decode()
    c.send(f"Acknowledgement of frame {ack} Recieved".encode())
c.close()









