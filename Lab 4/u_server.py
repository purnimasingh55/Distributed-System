import datetime
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
    print('Client Request :' + data.decode())
    if ('quit' in data.decode()) or not data:
        print("Server Exiting")
        conn.close()
        break
    elif('time' in data.decode()):
        x = datetime.datetime.now()
        print ("Current time :", end = ' ')
        print(x.year, end = '-')
        print(x.month, end = '-')
        print(x.day, end = ' ')
        print(x.strftime("%A"))
        st = (str(x.year) + '-' + str(x.month) + '-' + str(x.day) + '-' + x.strftime("%A"))
        conn.sendall(st.encode())
    else:
        print('Type your response:',end='')
        st=input()
        conn.sendall(st.encode())
conn.close()