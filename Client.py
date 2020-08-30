"""
PROGRAMMING ASSIGNMENT 1
BLAKE STANGER & JUSTIN GUERRERO
CSCI 466 DR. MIKE WITTIE
DUE 9/11/2020
"""


"""
CLIENT REQUIREMENTS
SEND A  R P OR S MESSAGE W/ UNIQUE IDENTIFICATION.
CHECK RESULT OF PLAY- DISPLAY TO USER. (W OR L)
CHECK W/L RECORD AND DISPLAY
RESET- CLEAR W/L RECORD.

needs to accept ip address and port of server process
python client.py 128.111.52.245 5000
"""


import socket
import pickle
import sys

class Client:

    HEADERSIZE = 10

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socket.gethostname(), 1234))

    while True:

        full_msg = b''
        new_msg = True
        while True:
            msg = s.recv(16)
            if new_msg:
                print(f"new message length: {msg[:HEADERSIZE]}")
                msglen = int(msg[:HEADERSIZE])
                new_msg = False

            full_msg += msg

            if len(full_msg) - HEADERSIZE == msglen:
                print("full msg recieved")
                print(full_msg[HEADERSIZE:])

                d = pickle.loads(full_msg[HEADERSIZE:])
                new_msg = True
                full_msg = b''


    print(full_msg)






