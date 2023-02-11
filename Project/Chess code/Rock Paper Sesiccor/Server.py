import socket
from _thread import *
import pickle
from game import Game

server = "10.1.85.173"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")

connected = set() #
games = {}   #going to store the dictionary abt the game gameid as key and gameobject as value
idCount = 0


def threaded_client(conn, p, gameId):
    global idCount
    conn.send(str.encode(str(p))) #to know if it's player1 or 0

    reply = ""
    while True:
        try:
            data = conn.recv(4096).decode()

            if gameId in games: #checking if gameId is still in the dictionary
                game = games[gameId]

                if not data:
                    break
                else:
                    if data == "reset":
                        game.resetWent()
                    elif data != "get": #move
                        game.play(p, data)

                    conn.sendall(pickle.dumps(game))
            else:
                break
        except:
            break

    print("Lost connection")
    try:
        del games[gameId]
        print("Closing Game", gameId)
    except:
        pass
    idCount -= 1
    conn.close()



while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    idCount += 1
    p = 0 #current player
    gameId = (idCount - 1)//2
    if idCount % 2 == 1:
        #we need to create a new game
        games[gameId] = Game(gameId)
        print("Creating a new game...")
    else:
        games[gameId].ready = True
        #both the players are connected and are ready to play
        p = 1 #players = 1


    start_new_thread(threaded_client, (conn, p, gameId))