import socket
import sys
from http.server import HTTPServer, BaseHTTPRequestHandler
import http.server
import requests
import threading
# BUFFER_SIZE = 1024
HOST = sys.argv[1]
PORT = int(sys.argv[2])
string = 'http://'+HOST+':'+sys.argv[2]
class Server(BaseHTTPRequestHandler):
    def game_header(self, move, response=''):
        self.send_response(move, response)
        self.end_headers()
    def bad_request(self):
        self.game_header(400, 'bad request')
    def rock(self):
        self.game_header(200, 'rock')

    def paper(self):
        self.game_header(200, 'paper')

    def scissors(self):
        self.game_header(200, 'scissors')

    def who_won(self, data):
        if(self.move == 'rock'):
            print("do stuff")
        elif(self.move == 'paper'):
            print("do stuff")
        elif(self.move == 'scissors'):
            print("do stuff")
        elif (self.move != 'rock' or 'scissors' or 'paper'):
            print("do stuff")

        else:
            self.bad_request()
    def do_POST(self):
        r = requests.post('http://localhost:'+PORT, data= {'wittie is a ' : 'chicken'})
        print(r)
        self.who_won(r)

    def do_GET(self):
        print(self.path)
        if




























# #    HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
# #    PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
#
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#         s.bind((HOST, PORT))
#         s.listen()
#         conn, addr = s.accept()
#         with conn:
#             print('Connected by', addr)
#             while True:
#                 print('here')
#                 data = conn.recv(1024)
#                 print('connection')
#                 r = requests.post(string)
#                 print('request was sent')
#                 r = requests.get(string)
#                 if not data:
#                     print('breaking')
#                     break
#                 conn.sendall(data)
#
#


#     def socketStuff(self):
#         file = open("newFile.txt", "a")
#         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         s.bind((host, port))
#         print('binded')
#         while(1):
#             s.listen()
#             print('listening...\n')
#             conn, addr = s.accept()
#             print('accepted the connection \n')
#             with conn:
#                 print("Connected with " , addr)
#                 while True:
#                     data = conn.recv(BUFFER_SIZE)
#                     conn.send(data)  # echo
#                     if not data:
#                         break
#                     conn.sendall(data)
#             x = requests.get(string)
#             print(x.text)
#             print(data)
#             print(BUFFER_SIZE)
#             newData = data.decode('utf-8')
#             file.write(newData + '\n')
#             file.close()
#
#             def do_post():
#                 print("posted up")
#
#         conn.close()
#     # def do_get(self):
#     #     self.
# class main():
#     Server().socketStuff()

    #     def __init__(self, my_ip, opp_ip):
    #         threading.Thread.__init__(self)
    #         self.my_ip = my_ip
    #         self.opp_ip = opp_ip
    #         self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #         self.s.bind(self.my_ip)
    #
    #     def respond(self, message):
    #         print("this test made it this far")
    #         self.conn.send(str(message).encode('utf-8'))
    #
    #     def run(self):
    #         while True:
    #             print("Listening....")
    #             self.s.listen(1)
    #             print('here')
    #             self.conn, self.address = self.s.accept()
    #             print('now here')
    #             receive = self.conn.recv(64)
    #             print(receive)
    #             response = self.bytes("hello", 'utf-8')
    #             self.respond(response)
    #             self.conn.close()