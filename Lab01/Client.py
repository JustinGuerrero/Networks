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

import http.client
import http.client
import http.server

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

import sys
import socket
import http.client

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
class Client:
    PLAYER_NUMBER = "UNASSIGNED"

    def __init__(self):
        h1 = http.client.HTTPConnection(sys.argv[1], int(sys.argv[2]))


    def run(self):
        self.assign_player_number(self)
        wanna_keep_playing = True
        while(wanna_keep_playing):
            print("WELCOME TO  ROCK PAPER SCISSORS")
            print("PLEASE SELECT: 1: QUIT, 2: RESET, 3: GET SCORE, 4: ROCK, 5: PAPER, 6: SCISSORS 7: GET RESULT")
            selector = input("SELECT:")

            #if(selector != 1 or 2 or 3 or 4 or 5 or 6 ):
                #print("BAD SELECTION TRY AGAIN")

            if(selector == 1):
                wanna_keep_playing = False
                exit()
            print("You selected option " + selector)
            self.select_switch(self, selector)

    def select_switch(self, argument):
        #print("switch")
        switcher = {"2": "RESET",
                    "3": "GET SCORE",
                    "4": "ROCK",
                    "5": "PAPER",
                    "6": "SCISSORS",
                    "7": "GET RESULT"
                    }

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
        elif(call_this=='GET RESULT'):
            self.getResult(self)
    def getResult(self):
        print("getting score: \n")
        h1 = http.client.HTTPConnection(sys.argv[1], int(sys.argv[2]))
        h1.request("GET", "/WhoWon.txt")  # http://192.168.56.1:1234
        #print('1')
        y = h1.getresponse()
        z = y.read().decode('utf-8')
        print(z)

    def getScore(self):
        print("Score of the game is: ")
        h1 = http.client.HTTPConnection(sys.argv[1], int(sys.argv[2]))
        h1.request("GET", "/score.txt")  # http://192.168.56.1:1234
        #print('1')
        y = h1.getresponse()
        z = y.read().decode('utf-8')
        print(z)

    def ROCK(self):
        print("ROCK")
        h1 = http.client.HTTPConnection(sys.argv[1], int(sys.argv[2]))
        h1.request("POST", "http://localhost:8000", body="{} rock ".format(self.PLAYER_NUMBER))
        print(h1.getresponse().msg)

    def PAPER(self):
        print("PAPER")
        h1 = http.client.HTTPConnection(sys.argv[1], int(sys.argv[2]))
        h1.request("POST", "http://localhost:8000", body="{} paper".format(self.PLAYER_NUMBER))
        print(h1.getresponse().msg)

    def SCISSORS(self):
        print("Scissors")
        h1 = http.client.HTTPConnection(sys.argv[1], int(sys.argv[2]))
        h1.request("POST", "http://localhost:8000", body="{} scissors ".format(self.PLAYER_NUMBER))
        print(h1.getresponse().msg)

    def RESET(self):
        print("made to reset")
        h1 = http.client.HTTPConnection(sys.argv[1], int(sys.argv[2]))
        h1.request("POST", "/newFile1", body="{} I WOULD LIKE TO RESET THE GAME".format(self.PLAYER_NUMBER))
        h2 = http.client.HTTPConnection(sys.argv[1], int(sys.argv[2]))
        h2.request("GET", "/newFile1.txt")
        y = h2.getresponse()
        z = y.read().decode('utf-8')
        print(z)
        play = input("keep playing? 1 for yes 0 for no\n")
        if(play == '1'):
            print("continuing...")
            print("No reset has been triggered, continue playing. ")
            return
        else:
            print("Opponent has agreed. ")
            print("please reconnect when you wish to continue playing.")
            exit(1)

    # def assign_player_number_two(self):
    #     if(self.PLAYER_NUMBER=="0"):
    #         self.PLAYER_NUMBER = "1"

    def assign_player_number(self):
        print("assigning a player ID")
        h1 = http.client.HTTPConnection(sys.argv[1], int(sys.argv[2]))
        h1.request("GET", "/newFile1.txt")  # http://192.168.56.1:1234

        y = h1.getresponse()
        z = y.read().decode('utf-8')
        print(z)
        print("this is player number compare", z)
        if(z==""):
            self.PLAYER_NUMBER=0
        elif(z!=""):
            self.PLAYER_NUMBER=1
        print(self.PLAYER_NUMBER)




if __name__ == "__main__":
    client = Client
    client.run(client)

