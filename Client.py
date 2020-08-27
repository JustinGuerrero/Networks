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


import socket as s

HOST = '127.0.0.1'
PORT = 8080


with s.socket(s.AF_INET, s.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)


