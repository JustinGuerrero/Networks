"""
PROGRAMMING ASSIGNMENT 1
BLAKE STANGER & JUSTIN GUERRERO
CSCI 466 DR. MIKE WITTIE
DUE 9/11/2020
"""

"""
SERVER REQUIREMENTS

ON START UP ACCEPT A PORT PARAMETER, THAT CLIENTS CONNECT TO (python server.PY 5000)
"""


import socket
import time
import pickle
import sys

class Server:

    def runServer(self):
        HEADERSIZE = 10


        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((socket.gethostname(), int(sys.argv[1])))
        print(socket.gethostname())
        s.listen(1000)

        while True:
            clientsocket, address = s.accept()
            print(f"connection from {address} has been established..")

            d = {1: "hi", 2: "sacrifice at the alter!"}

            msg = pickle.dumps(d)


            msg = bytes(f'{len(msg): < {HEADERSIZE}}', "utf-8" )+ msg

            clientsocket.send(msg)



smash = Server
smash.runServer(smash)
