'''import socket
c=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#c.recv(10)
emsg = "Hello"
ecd = str.encode(emsg)
add = ("localhost",54000)
c.sendto(ecd,add)
a = c.recvfrom(1000)
print("Recieved msg from server.",a)
#c.sendto(bytes("Pass the msg"))'''

'''import  socket
c = socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
add = ('localhost',6788)
msg = "hello"
ecm = str.encode("Hellp")
c.sendto(ecm,add)
#b = c.recvfrom(1000)
print("Server msg is: ")
c.close()'''

import socket
import time
from threading import *
c = socket.socket()
c.connect(('localhost',6776))
class Byee(Thread):
    def run(self):
        for i in range(5):
            #print("byee")
            msg="hello"
            c.send(msg.encode())
            time.sleep(1)
            a = c.recv(2000)
            print(f"server: ",a.decode())
t1 = Byee()
t1.start()
c.close()
            

