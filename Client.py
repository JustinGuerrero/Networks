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
import time

import requests
import secrets
import http.client, urllib.parse, codecs
import http.client
import sys
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
import sys
import urllib3
import socket
import http.client
import pickle
yat= "POST "
PLAYERNUMBER = 1234
play = 1

print("my player number is :", PLAYERNUMBER)

while(play == 1):


    print("Welcome to ROCK, PAPER, SCISSORS!")
    yat = yat + input("OPTIONS: ROCK, PAPER, SCISSORS GETSCORE QUIT RESET Please enter your play: ")
    if(yat =="QUIT"):
        play = 0

    if(yat == "POST RESET"):
        yat = "POST RESET " + PLAYERNUMBER
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((sys.argv[1], int(sys.argv[2])))
        s.send(bytes(yat + " ", "utf-8"))
        data = s.recv(1024)
        print(data)
        continue


    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((sys.argv[1], int(sys.argv[2])))
    if(PLAYERNUMBER ==1):
        s.send(bytes(yat + " \n", "utf-8"))
    s.send(bytes(yat+" ", "utf-8"))
    data = s.recv(1024)
    if (data == b'0'):
        PLAYERNUMBER = 0
    elif(data == b'1'):
        PLAYERNUMBER = 1

    print("MY PLAYER NUMBER IS: ", PLAYERNUMBER)
    print(data)
    s.close()
    time.sleep(10)



# print(PLAYS)



# justin = sys.argv[1]
# port = int(sys.argv[2])
# string = "http://"+justin + ":" + sys.argv[2]
#
# r = requests.get(string)
#
# print(r.status_code)
#
# print(r.headers)
#
# print(r.url)









# class Client:
#
#     h1= http.client.HTTPConnection(justin, port)
#
#
#     HEADERSIZE = 10
#     server = (sys.argv[1], int(sys.argv[2]))
#     # s.bind((justin, port))
#     s.connect(((sys.argv[1]), port))  #connect (ipadress, port)
#     message = input("->")
#     while True:
#         s.sendto(message.encode('utf-8'), server)
#         data, addr = s.recvfrom(port)
#         data = data.decode('utf-8')
#         print("received from server: " + data)
#         message = input("->")
#     sys.exit
#
#     print(full_msg)







# conn = http.client.HTTPConnection(sys.argv[1], int(sys.argv[2]))
# conn.request("GET", string)
# r1= conn.getresponse()
# print(r1.status, r1.reason)
# print ("fuck")




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





#cite your sources: https://stackoverflow.com/questions/8107177/using-python-requests-library-to-post-a-text-file


