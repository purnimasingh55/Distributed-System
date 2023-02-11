'''import socket
import time
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind(('localhost',1900))
s.listen(5)
currtime = time.ctime(time.time())
print(currtime)
fn = 'mytext.txt'
f=open(fn,'r')
s = f.read(2000)
c, c_add = s.accept()
while(s):

    c.send(bytes(s))
    f.close()
    data = c.recv(500).decode()
    c.close()
'''

import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostname()
port=9808
s.bind((host,port))
s.listen(5)
print('server is started')
while True:
    c,caddr=s.accept()
    print(caddr)
    data=c.recv(2000)
    print(data.decode())
    fn='mytxt.txt'
    f=open(fn,'rb')
    m=f.read(2000)
    while(m):
        print(c.send(bytes(str(m), 'utf-8')))
        m = f.read(2000)
    f.close()
    print('sending completed')
    #c.send(bytes('connected', 'utf-8'))
    c.close()

'''import socket

s = socket.socket()
host  =socket.gethostname()
port  = 9089
s.bind(host,port)
s.listen(1)
print("Server strted")
while True:
    c,cadd = s.accept()
    print(cadd)
    fn = "text.txt"
    f = open('mytxt.txt','rb')
    m = f.read(2000)
    while m:
        m = f.read(2000)
    f.close()
    print("Sending competed")
    c.close()'''
