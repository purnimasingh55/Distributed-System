from socket import *

client=socket()

client.connect(('localhost',6001))

print(client.recv(1024).decode())

k=int(input())

client.close()