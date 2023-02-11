import socket
c = socket.socket(family = socket.AF_INET , type = socket.SOCK_STREAM)
c.connect(('localhost',4899))
l = [1,2,3,4,5,6,7]
while(1):
    sh = input("Is co-ordinator working?? Give answer in True or False ")
    if (sh == True):
        pass
    else:
        ch = int(input("Enter the process at which co-ordinator failed"))
        c.election(l, ch)
c.close()




