'''import socket
s = socket.socket(family = socket.AF_INET , type = socket.SOCK_STREAM)

l =[1,2,3,4,5,6,7]
cordinator = max(l)
s.bind(('localhost',4899))
s.listen(5)

def election(l,ch):
    l.pop()
    l = l[ch-1::]
    cordinator = max(l)

c, addr = s.accept()
el = election(l,c.ch)
s.send(s.el)'''






