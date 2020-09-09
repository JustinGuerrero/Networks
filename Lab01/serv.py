import socket
import sys
import http.server
import requests
import threading
BUFFER_SIZE = 1024
host = sys.argv[1]
port = int(sys.argv[2])
string = 'http://'+host+':'+sys.argv[2]
class Server(threading.Thread):
    def socketStuff(self):
        while(1):
            file = open("newFile.txt", "a")
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.bind((host, port))
            s.listen(1)
            conn, addr = s.accept()
            x = requests.get(string)
            print(x.text)
            data = conn.recv(BUFFER_SIZE)
            conn.send(data) #echo
            print(data)
            print(BUFFER_SIZE)
            newData = data.decode('utf-8')
            file.write(newData + '\n')
            file.close()

            def do_post():
                print("posted up")

        conn.close()
    # def do_get(self):
    #     self.
class main():
    Server().socketStuff()

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