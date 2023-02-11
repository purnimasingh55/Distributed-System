import socket
s = socket.socket()
s.connect(('127.0.0.1',15000))
while True:
    print("Type in your request: ",end='')
    num = input()
    if num=='quit':
        s.close()
        break
    s.send(num.encode())
    data = s.recv(1024).decode()
    print('This is the response: '+data)
