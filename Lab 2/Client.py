'''import socket
import time
c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c.connect(('localhost',1900))
ct = time.ctime(time.time())
print(ct)
with open('mytxt.txt','w') as f:
    while True:
        data = c.recv(2000)
        print(data)
        c.send(bytes("Pass the file"))
        if not data:
            print("Content not in file")
            break
    f.write(data)
f.close()
c.close()

'''



'''import socket
c=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostname()
port=9808
c.connect((host,port))
c.send(bytes('hi server','utf-8'))

with open('mytxt1.txt','wb') as f:
    print('file is opened')
    while True:
        data=c.recv(2000)
        print(data)
        if not data:
           break
        f.write(data)
f.close()
print('Successfully get the file')
c.close()
print('connection closed')'''

import  socket
c = socket.socket()
host = socket.gethostname()
port = 9808
c.connect(host,port)
c.send(bytes("Hii",'utf-8'))

with open('mytxt.txt','wb') as f:
    while True:
        data = c.recv(2000)
        if not data:
            break
        f.write(data)
f.close()


