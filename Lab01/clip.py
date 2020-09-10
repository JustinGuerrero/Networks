import os
import socket
import sys
import threading
import http.client
import time
import requests

# BUFFER_SIZE = 1024
HOST = sys.argv[1]
PORT = int(sys.argv[2])
string = 'http://'+HOST+':'+sys.argv[2]

class myClient():
   #print(string)

 #  HOST = '127.0.0.1'  # The server's hostname or IP address
 #  PORT = 65432  # The port used by the server

   with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      s.connect((HOST, PORT))
      s.sendall(b'Hello, world')
      r = requests.get(string)
      r1 = requests.post(string, {'justin':'rock'})
      data = s.recv(1024)

   print('received', repr(data))

 #   print('Received', repr(data))
 # #  print("Put some stupid thing here")
 # #   answer = input()
 #    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 #    s.connect((host, port))
 #    s.sendall(bytes("test", 'utf-8'))
 #    data = s.recv(BUFFER_SIZE)
 #    data2 = data.decode('utf-8')
 #    r = requests.post(host + ":" + str(port), data2)
 #    print(data2)
 #    s.close()
 #
 #

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