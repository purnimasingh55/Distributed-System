'''import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
host = socket.gethostname()
print(host)
add = ("localhost",54000)
adds = 54000
s.bind(('localhost',adds))
a = s.recvfrom(1000)
print("This is client msg.",a)
emsg = "Hello"
ecd = str.encode(emsg)
s.sendto(ecd,add)'''
'''
import  socket
s = socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
add = ('localhost',6788)
s.bind((add))
a = s.recvfrom(1000)
print("Cleint msg is: ",a)
#em2 = str.encode("Msg Recvd")
#s.sendto(em2,add)
s.close()'''

'''import time
import socket
from threading import *
s = socket.socket()
s.bind(('localhost',6776))
s.listen(1)
c, cadd = s.accept()
class Hi(Thread):
    def run(self):
        for i in range(5):
            b  = c.recv(2000)
            print("Client",b.decode())
            #print("hi")
            c.send(bytes("Hii",'utf-8'))
            time.sleep(1)
t2 = Hi()
t2.start()
c.close()
            '''



