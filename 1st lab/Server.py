import socket
s = socket.socket(family = socket.AF_INET , type = socket.SOCK_STREAM)
#port =1800
s.bind(('localhost',1800))
#(ipaddress,port address)  127.0.0.1 Local host ipaddress
''' Port address must not be greater then 65000 and less than 1024'''
s.listen(5)
print("Wait")



#s.accept(c,c_add) #(client,client address)
c, c_add = s.accept()
print(c_add)
#data = c.recv(500).encode()
data = c.recv(500).decode()
#c1.close()
c.close()
#s.close()  #server file must not be closed

