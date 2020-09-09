import os
import socket
import sys
import threading
import http.client
import time
import requests

BUFFER_SIZE = 1024
host = sys.argv[1]
port = int(sys.argv[2])
string = 'http://'+host+':'+sys.argv[2]

class myClient():

 #  print("Put some stupid thing here")
 #   answer = input()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.connect((host, port))
    s.send(bytes("test", 'utf-8'))
    data = s.recv(BUFFER_SIZE)
    data2 = data.decode('utf-8')
    # r = requests.post("http://" + host + ":" + '8000', data2)
    print(data2)
    s.close()



# class Client(threading.Thread):
#   def __init__(self, my_server, opp_server):
#     self.my_server = my_server
#     self.opp_server = opp_server
#
#   def update_server(self, data):
#     response = data.decode('utf-8')
#     print("we got the message here")
#     filepath = os.path.join('game.txt')
#     here = open(filepath, 'r')
#     here.close()
#
#
#
#   def connect_opp_server(self):
#     print("top of connect")
#     self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     while True:
#       time.sleep(1)
#       print("Trying to connect...." + str(self.my_server))
#       try:
#         self.s.connect((self.my_server))
#         print('i have connected')
#         break
#       except Exception as e:
#         print('Waiting for server: '), e
#
#   def run(self):
#     while True:
#       data = self.s.recv(64)
#       self.s.close()
#
#       time.sleep(1)
#     else:
#        time.sleep(1)