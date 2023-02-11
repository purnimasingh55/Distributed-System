''''
import socket
def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 5000  # initiate port no above 1024
    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together
    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        print("from connected user: " + str(data))
        data = input(' -> ')
        conn.send(data.encode())  # send data to the client

    conn.close()  # close the connection
if __name__ == '__main__':
    server_program()
'''



'''' 

import socket
s = socket.socket()
host = socket.gethostname()
port = 5000
s.bind(host,port)
'''

from threading import Thread
import socket
addr_client = {}
clients  = {}
count = 0
def incoming_connection():
    while True:
        conn, client_addr = s.accept()
        print(client_addr)
        print(conn)
        addr_client[conn] = client_addr
        print (conn)
        Thread(target = client_connection, args = (conn,)).start()


def client_connection(conn):
    name = conn.recv(100).decode("utf8")
    clients[conn] = name

    while True:
        msg = conn.recv(100).decode("utf8")
        broadcast(msg,name+":")


def broadcast(msg,prefix):
    for sock in clients:
        #print(prefix)
        sock.send(bytes(prefix+msg,"utf8"))


host = 'localhost'
port = 12345
addr = (host,port)
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind(addr)

s.listen(5)
print ("waiting for connection")
Thread (target = incoming_connection).start()
#Thread (target = incoming_connection).join()




