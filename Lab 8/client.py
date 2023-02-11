import socket

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect(('localhost',5900))

print("Connected !!")

server_data1=client.recv(1024).decode()
print(server_data1)
k=input()
client.sendall(k.encode())
server_data2=client.recv(1024).decode()
print(server_data2)
m=input()
client.sendall(m.encode())
server_data3=client.recv(1024).decode()
print(server_data3)
l=input()
client.sendall(l.encode())
server_data4=client.recv(1024).decode()
print(server_data4)
client.close()