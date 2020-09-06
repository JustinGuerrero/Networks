"""
PROGRAMMING ASSIGNMENT 1
BLAKE STANGER & JUSTIN GUERRERO
CSCI 466 DR. MIKE WITTIE
DUE 9/11/2020
"""

"""
SERVER REQUIREMENTS

ON START UP ACCEPT A PORT PARAMETER, THAT CLIENTS CONNECT TO (python server.PY 5000)
"""

from http.server import HTTPServer, BaseHTTPRequestHandler, CGIHTTPRequestHandler
import socket
import pickle
import sys
import cgi
from urllib.parse import urlparse
from routes.main import routes



class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('somestuff', 'text/html')
        self.end_headers()
        self.wfile("hello blake!".encode())

    def handle_http(self, status, content_type):
        self.send_response(status)
        self.send_header('Content-type', content_type)
        self.end_headers()
        route_content = routes[self.path]
        return bytes(route_content, "UTF - 8")


    def run(self, server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
        server_address = (sys.argv[1], int(sys.argv[2]))
        print("UP AND SERVIN SHIT AT: " + sys.argv[1]+" : "+ sys.argv[2]+ "!")


        httpd = server_class(server_address, handler_class)
        httpd.serve_forever()


    # def do_POST(self):
    #
    #         print("Oh boy Here I go postin' again")
    #         length = int(self.headers.getheader('content-length'))
    #         field_data = self.rfile.read(length)
    #         fields = urlparse.parse_qs(field_data)
    #
    # def do_GET(self, handlerclass):
    #     self.send_response(200)



            #data_file = fields["data.txt"]


# class Server:
#         def runServer(self):
#             HEADERSIZE = 10
#
#             s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#             s.bind((socket.gethostname(), int(sys.argv[1])))
#             print(socket.gethostname())
#             victory = socket.gethostname()
#             print(socket.gethostbyname(victory))
#             s.listen(5)
#
#             while True:
#                 clientsocket, address = s.accept()
#                 print(f"connection from {address} has been established..")
#                 d = {1: "hi", 2: "Fire!"}
#                 msg = pickle.dumps(d)
#                 msg = bytes(f'{len(msg): < {HEADERSIZE}}', "utf-8") + msg
#                 clientsocket.send(msg)
#

# CITE YOUR SOURCES https://stackoverflow.com/questions/2490162/parse-http-get-and-post-parameters-from-basehttphandler/31363982#31363982

smash = Server()
smash.run()