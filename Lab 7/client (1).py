from socket import *

client=socket()

client.connect(('localhost',9001))

print(client.recv(1024).decode())
n=int(input())
n=str(n)
client.send(n.encode())
print(client.recv(1024).decode())
k=int(input())
k=str(k)
client.send(k.encode())
for i in range(int(n)):
    print(client.recv(1024).decode())
    ack=client.recv(1024).decode()
    client.send(f"ACKNOWLEDGEMENT of Frame {ack} Recived".encode())
client.close()