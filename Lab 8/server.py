import socket
import sys
def cord(n,f,s):
    l=[]
    for i in range(n):
        l.append(i+1)
    print(f"The List the Nodes Present are:{l}")
    l.remove(f)
    print(f"The Present Cordinator {f} is Not Working !!")
    index = l.index(s)
    print(f"Election Started By {s}")

    if l[index] == l[-1]:
        print(l[-1])
        sys.exit()

    e = 0
    for i in range(index,len(l)):
        for j in range(i+1,len(l)):
            print(f"Election {e} Request sent from {l[i]} to {l[j]}")
        e += 1
        print("\n")
    print(f"The New Cordinator is :{max(l)}")
    return (max(l))


server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind(('localhost',5900))

server.listen(1)

print("Waiting for Connection ......\n")

connection, address = server.accept()

print(f"\nConnected to {address}")

connection.sendall("Enter the No of Nodes :".encode())
client_data1=int(connection.recv(1024).decode())
print(f"Client:{client_data1}")

connection.sendall("Enter the Node Number That Failed:".encode())
client_data2=int(connection.recv(1024).decode())
print(f"Client:{client_data2}")
connection.sendall("Enter the Node Number That started Election :".encode())
client_data3=int(connection.recv(1024).decode())
print(f"Client:{client_data3}")
res = cord(client_data1,client_data2,client_data3)
connection.sendall(f"The new Cordinator is {res}".encode())
connection.close()