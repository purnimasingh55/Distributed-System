import socket
s = socket.socket()
host = socket.gethostname()
port = 9809
s.bind((host,port))
s.listen()

print("Waiting for the acknolegdements: ")

c, cadd = s.accept()
print("Connected to client: ",cadd)
c.send("Enter the total no. of frames to be send: ".encode())

n = c.recv(1024).decode()

n = int(n)
print(n)

c.send("Enter Window size".encode())
m = c.recv(1024).decode()
m = int(m)
print(m)

for i in range(int(n)):
    c.send(f"Frame Number {i % int(m)} Data : {i+1}".encode())
    c.send(str(i % m).encode())
    print(c.recv(1024).decode())


s.close()


