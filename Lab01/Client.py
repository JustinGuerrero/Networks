"""
PROGRAMMING ASSIGNMENT 1
BLAKE STANGER & JUSTIN GUERRERO
CSCI 466 DR. MIKE WITTIE
DUE 9/11/2020
"""
import http

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

import requests
import secrets
import http.client, urllib.parse

string = "http://"+ sys.argv[1] + ":" + sys.argv[2]
print(string)



conn = http.client.HTTPConnection(sys.argv[1], int(sys.argv[2]))
conn.request("GET", string)
r1= conn.getresponse()
print(r1.status, r1.reason)




#conn.request("POST", string, 'game.txt')
# r = conn.getresponse()
# print(r)

# class Client:
#
#     print("Welcome to Rock, Paper, Scissors")
#     val = input("Please enter your play")
#     print(val)
#
#     number = secrets.randbelow(25)
#     ip = sys.argv[1]
#     port = sys.argv[2]
#     string = "walrus"
#     print (string)
#
#
#
#     if(val=="rock"):
#         requests.put(string)
#         print(number)


    # HEADERSIZE = 10
    # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # s.connect(((sys.argv[1]), int(sys.argv[2])))  # connect (ipadress, port)




    # while True:
    #
    #     full_msg = b''
    #     new_msg = True
    #     while True:
    #         msg = s.recv(1024)
    #         if new_msg:
    #             print(f"new message length: {msg[:HEADERSIZE]}")
    #             msglen = int(msg[:HEADERSIZE])
    #             new_msg = False
    #         full_msg += msg
    #         if len(full_msg) - HEADERSIZE == msglen:
    #             print("full msg recieved")
    #             #print(full_msg[HEADERSIZE:])
    #             d = pickle.loads(full_msg[HEADERSIZE:])
    #             new_msg = True
    #             full_msg = b''
    # print(full_msg)








