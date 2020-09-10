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
import requests

class Client:
    PLAYER_NUMBER = "UNASSIGNED"

    def __init__(self):
        h1 = http.client.HTTPConnection(sys.argv[1], int(sys.argv[2]))


    def run(self):
        wanna_keep_playing = True
        while(wanna_keep_playing):
            print("WELCOME TO  ROCK PAPER SCISSORS")
            print("PLEASE SELECT: 1: QUIT, 2: RESET, 3: GET SCORE, 4: ROCK, 5: PAPER, 6: SCISSORS")
            selector = input("SELECT:")
            self.select_switch(self, selector)

            if(selector!= '1' or "2" or "3" or "4" or "5" or "6" ):
                print("BAD SELECTION TRY AGAIN")
                continue
            if(selector == "1"):
                wanna_keep_playing = False
                continue
            print(selector)




    def select_switch(self, argument):
        print("switch")
        switcher = {"2": "RESET",
                    "3": "GET SCORE",
                    "4": "ROCK",
                    "5": "PAPER",
                    "6": "SCISSORS"}

        call_this = switcher.get(argument)
        if(call_this=="GET SCORE"):
            self.getScore(self)
        elif(call_this=="RESET"):
            self.RESET(self)
        elif(call_this=="ROCK"):
            self.ROCK(self)
        elif(call_this=="PAPER"):
            self.PAPER(self)
        elif(call_this=="SCISSORS"):
            self.SCISSORS(self)


    def getScore(self):
        print("made get score")
        h1 = http.client.HTTPConnection(sys.argv[1], int(sys.argv[2]))
        h1.request("GET", "/score.txt")  # http://192.168.56.1:1234
        print('1')
        y = self.h1.getresponse()
        z = y.read()
        print(z)

    def ROCK(self):
        print("ROCK")
        h1 = http.client.HTTPConnection(sys.argv[1], int(sys.argv[2]))
        h1.request("POST", "/game.txt", body="{}:rock".format(self.PLAYER_NUMBER))
        print(h1.getresponse().msg)

    def PAPER(self):
        print("PAPER")
        h1 = http.client.HTTPConnection(sys.argv[1], int(sys.argv[2]))
        h1.request("POST", "/Player_Nos.txt", body="{}:paper".format(self.PLAYER_NUMBER))
        print(h1.getresponse().msg)

    def SCISSORS(self):
        print("Scissors")
        h1 = http.client.HTTPConnection(sys.argv[1], int(sys.argv[2]))
        h1.request("POST", "/game.txt", body="{}:scissors6".format(self.PLAYER_NUMBER))
        print(h1.getresponse().msg)

    def RESET(self):
        print("made to reset")
        h1 = http.client.HTTPConnection(sys.argv[1], int(sys.argv[2]))
        h1.request("POST", "/game.txt", body="{}:reset".format(self.PLAYER_NUMBER))
        print(h1.getresponse().msg)

    def assign_player_number(self):
        print("made get score")
        h1 = http.client.HTTPConnection(sys.argv[1], int(sys.argv[2]))
        h1.request("GET", "/score.txt")  # http://192.168.56.1:1234
        print('1')
        y = h1.getresponse()
        z = y.read()
        print(z)



    # def run(self):
    #     wanna_keep_playing = True
    #     while (wanna_keep_playing):
    #         print("WELCOME TO  ROCK PAPER SCISSORS")
    #         print("PLEASE SELECT: 1: QUIT, 2: RESET, 3: GET SCORE, 4: ROCK, 5: PAPER, 6: SCISSORS")
    #         y = input("SELECT:")
    #         if (y == 1):
    #             wanna_keep_playing = False
    #             continue



if __name__ == "__main__":
    client = Client
    client.run(client)



# body= "***send this stuff***"
#         self.h1.request("GET", "/Player_Nos2.txt") #http://192.168.56.1:1234
#         print('1')
#         y = self.h1.getresponse()
#
#         z = y.read()
#
#         print(z)
#
#         url = 'http://192.168.56.1:1234/Player_Nos.txt'
#         files = {'file': open('Player_2Nos', 'rb')}
#         print('2')
#
#         h1.request("POST", "/Player_Nos.txt", body="{player1:rock}")
#         print(h1.getresponse().msg)






#y= h1.getresponse()

#


#requests.post(url, data={'key':'value'})

#(r.text)


print('here')


#r.text
print('made it to print text')
#print(r.text)
#h1.request("POST", "/game.txt", "game.txt")




#
#
# PLAYERNUMBER = "UNASSIGNED"
#
#
#
#
# x = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# x.connect((sys.argv[1], int(sys.argv[2])))
# x.send(bytes("GET GAMEFILE \n" + " ", "utf-8"))
# data = x.recv(1024)
# x.close()
# print(data)
#
# # for x in range(3):
#
# print("HIT POST")
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect((sys.argv[1], int(sys.argv[2])))
# s.send(bytes("POST SCISSORS \n" + " ", "utf-8"))
# data = s.recv(1024)
# s.close()
# print(data)
#
#
# print("Start END")
# x = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# print("Past socket")
#
# x.connect((sys.argv[1], int(sys.argv[2])))
# print("past connect")
# x.send(bytes("OPTIONS GAMEFILE \n" + " ", "utf-8"))
# print("past send")
# data = x.recv(1024)
# print("past recieve")
# x.close()
# if(data==b'1'):
#     PLAYERNUMBER = "1"
# if(data==b'0'):
#     PLAYERNUMBER = "0"
# print(PLAYERNUMBER)
#
# print(data)
# print("GOT TO END")
#
#
#












#CLIENT OLD ATTEMPT
# yat= ""
# PLAYERNUMBER = 1234
# play = 1
#
# print("my player number is :", PLAYERNUMBER)
#
# while(play == 1):
#
#
#     print("Welcome to ROCK, PAPER, SCISSORS!")
#     yat = yat + input("OPTIONS: ROCK, PAPER, SCISSORS GETSCORE QUIT RESET Please enter your play: ")
#     if(yat =="QUIT"):
#         play = 0
#
#     if(yat == "POST RESET"):
#         yat = "POST RESET " + PLAYERNUMBER
#         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         s.connect((sys.argv[1], int(sys.argv[2])))
#         s.send(bytes(yat + " ", "utf-8"))
#         data = s.recv(1024)
#         print(data)
#         continue
#
#
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     s.connect((sys.argv[1], int(sys.argv[2])))
#     if(PLAYERNUMBER ==1):
#         s.send(bytes(yat + " \n", "utf-8"))
#     s.send(bytes(yat+" ", "utf-8"))
#     data = s.recv(1024)
#     if (data == b'0'):
#         PLAYERNUMBER = 0
#     elif(data == b'1'):
#         PLAYERNUMBER = 1
#
#     print("MY PLAYER NUMBER IS: ", PLAYERNUMBER)
#     print(data)
#     s.close()
#     time.sleep(10)



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
# print ("f")




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


