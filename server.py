import socket
from _thread import *
from player import Player
import pickle
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = '10.195.221.144'
port = 5555

server_ip = socket.gethostbyname(server)

players = [Player(0,0,(255,0,0)),Player(0,0,(0,255,0))]

try:
    s.bind((server, port))
except socket.error as e:
    print(str(e))

s.listen(2)


print("Waiting for a connection")

def threaded_client(conn, player):
    conn.send(pickle.dumps(players[player]))
    reply = ""

    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            players[player] = data

            if not data:
                print("Goodbye")
                break
            else:
                print("Recieved: " + reply)
                if player == 1:
                    reply = players[0]
                else:
                    reply = players[1]
                print("Sending: " + reply)

            conn.sendall(pickle.dumps(reply))
        except:
            break

    print("Connection Closed")
    conn.close()

currentPlayer = 0
while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1