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


justin = '192.168.153.1'
port = 1234
class Client:

    HEADERSIZE = 10
    server = (sys.argv[1], int(sys.argv[2]))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((justin, port))
    #s.connect(((sys.argv[1]), int(sys.argv[2])))  #connect (ipadress, port)
    message = input("->")
    while True:
        s.sendto(message.encode('utf-8'), server)
        data, addr = s.recvfrom(1234)
        data = data.decode('utf-8')
        print("received from server: " + data)
        message = input("->")
        #s.sendto("hey man", blake,port)
    sys.exit

    print(full_msg)






