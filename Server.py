import cgi
import sys
from http.server import HTTPServer, BaseHTTPRequestHandler
import http.server
import urllib.request
import os
# main.py
import pickle
import socket
from socket import *


def createServer():
    serversocket = socket(AF_INET, SOCK_STREAM)
    try:
        serversocket.bind((sys.argv[1], int(sys.argv[2])))
        serversocket.listen(5)
        while(1):
            (clientsocket, address) = serversocket.accept()
            rd= clientsocket.recv(5000).decode()
            pieces = rd.split(" ")
            print(pieces)
            print(pieces[0])

            if (pieces[0] == "POST"):
                    f = open("game.txt", "a")
                    data2 = pieces[1]
                    f.write(data2+" ")
                    f.close()
                    data2 = "202 ACCEPTED " +data2 + " WRITTEN TO GAME"
                    print(data2)
                    clientsocket.sendall(data2.encode())
                    clientsocket.shutdown(SHUT_WR)

            elif(pieces[0] == "GET"):
                    print("Hit GET")
                    with open("game.txt", "r") as gamefile:
                        data = "200 OK"
                        data += gamefile.read()
                        print("GAMEFILE DATA:",data)


                    clientsocket.sendall(data.encode())
                    clientsocket.shutdown(SHUT_WR)

            elif (pieces[0] == "OPTIONS"):
                print("Hit OPTIONS")
                with open("Player_Nos.txt", "r") as playerone_file:
                    dataoptions = playerone_file.read()
                    print("Player DATA:", dataoptions)
                    playerone_file.close()
                    if(dataoptions == "0N"):
                        with open("Player_Nos.txt", "w") as playerone_file_write:
                            playerone_file_write.write("0")
                            playerone_file_write.close()
                            playerone_number = "0"


                            clientsocket.sendall(playerone_number.encode())
                            clientsocket.shutdown(SHUT_WR)
                            continue
                    with open("Player_Nos2.txt", "r") as playertwo_file:
                        dataoptions2 = playertwo_file.read()
                        print("Player DATA:", dataoptions2)
                        playertwo_file.close()
                        if (dataoptions == "1N"):
                            with open("Player_Nos2.txt", "w") as playertwo_file_write:
                                playertwo_file_write.write("1")
                                playertwo_file_write.close()
                                playertwo_number = "1"

                                clientsocket.sendall(playertwo_number.encode())
                                clientsocket.shutdown(SHUT_WR)
                                continue



                clientsocket.sendall(data.encode())
                clientsocket.shutdown(SHUT_WR)

            else:
                data = "501 NOT IMPLEMENTED"
                clientsocket.sendall(data.encode())
                clientsocket.shutdown(SHUT_WR)
    except KeyboardInterrupt:
            print("\nShutting down...\n");
    # except Exception as exc:
    #         print("Error:\n");
    #         print(exc)
    #
    #  serversocket.close()




# print('Access http://localhost:9000')
createServer()







# class Server(BaseHTTPRequestHandler):
#
#     def do_GET(self):
#         if self.path == '/':
#             self.path = "/index.html"
#         try:
#             file_to_open = open(self.path[1:]).read()
#             self.send_response(200)
#         except:
#             file_to_open = "File not found"
#             self.send_response(404)
#         self.end_headers()
#         self.wfile.write(bytes(file_to_open, 'utf-8'))
#
#     httpd = HTTPServer((sys.argv[1], int(sys.argv[2])), BaseHTTPRequestHandler)
#     print(httpd.server_address)
#     httpd.serve_forever()
#

# SERVER OLD ATTEMPT
#
# with open("win_dic", 'rb') as handle:
#     b = pickle.loads(handle.read())
#
# with open("Player_Nos", 'rb') as zandle:
#     c = pickle.loads(zandle.read())
#
# with open("Player_2Nos", 'rb') as xandle:
#     g = pickle.loads(xandle.read())
#
# print(c["ONE"])
#
# print(g["TWO"])
# BUFFER_SIZE = 10
# #
#
# while (1):
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     s.bind ((sys.argv[1], int(sys.argv[2])))
#     s.listen(2)
#
#     print("listening at", s.getsockname())
#     conn, addr = s.accept()
#     data = conn.recv(BUFFER_SIZE)
#
#     print("DATA IS: ", data)
#
#     f= open("game.txt", "a")
#     data2 = data.decode('utf-8')
#     print(data2)
#     f.write(data2)
#     f.close()
#     data2 = data2 + " WRITTEN TO GAME"
#     print(data2)
#
#     with open("Player_Nos", 'rb') as zandle:
#         c = pickle.loads(zandle.read())
#
#     with open("Player_2Nos", 'rb') as xandle:
#         g = pickle.loads(xandle.read())
#     print(c["ONE"], g["TWO"])
#     if (c["ONE"] == "0A"):
#         playerNos = {
#             "ONE": "0",
#             "RESET": "N"
#         }
#         with open("Player_Nos", "wb") as zapalm:
#             pickle.dump(playerNos, zapalm)
#             conn.send(b'0')
#
#     elif (g["TWO"] == "1A"):
#         playerNos2 = {
#             "TWO": "1",
#             "RESET": "N"
#         }
#         with open("Player_2Nos", "wb") as xapalm:
#             pickle.dump(playerNos2, xapalm)
#             conn.send(b'1')
#
#
#
#
#
#     conn.send(data) #echo
#     data = " "
#     conn.close()
#
# END OLD ATTEMPT.


# if __name__ == '__main__':
#


# CITE YOUR SOURCES

# I leaned heavily on this guys guide to building an HTTP server. He walked me through everything and I got most of the code here from him.
# I modifed things to work on the ROCK, PAPER, SCICCORS methods and needs for class.
# https://bhch.github.io/posts/2017/11/writing-an-http-server-from-scratch/
#
#
# class TCPServer:
#
#     def __init__(self):
#         self.host = sys.argv[1]  # address for our server
#         self.port = int(sys.argv[2]) # port for our server
#
#     def start(self):
#         # create a socket object
#         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#         # bind the socket object to the address and port
#         s.bind((self.host, self.port))
#         # start listening for connections
#         s.listen(5)
#
#
#         print("Listening at", s.getsockname())
#
#         while True:
#             # accept any new connection
#             conn, addr = s.accept()
#
#             print("Connected by", addr)
#
#             # read the data sent by the client (1024 bytes)
#             data = conn.recv(1024)
#
#             response = self.handle_request(data)
#
#             # send back the data to client
#             conn.sendall(response)
#
#             # close the connection
#             #conn.close()
#
#     def handle_request(self, data):
#         return data
#
#
# class HTTPServer(TCPServer):
#
#     headers = {
#         'Server': 'CrudeServer',
#         'Content-Type': 'text/html',
#     }
#
#     status_codes = {
#         200: 'OK',
#         404: 'Not Found',
#         501: 'Not Implemented',
#     }
#
#     def handle_request(self, data):
#         # create an instance of `HTTPRequest`
#         request = HTTPRequest(data)
#
#         # now, look at the request method and call the
#         # appropriate handler
#         try:
#             handler = getattr(self, 'handle_%s' % request.method)
#         except AttributeError:
#             handler = self.HTTP_501_handler
#
#         response = handler(request)
#
#         return response
#
#     def HTTP_501_handler(self, request):
#         response_line = self.response_line(status_code=501)
#
#         response_headers = self.response_headers()
#
#         blank_line = "\r\n"
#
#         response_body = "<h1>501 Not Implemented</h1>"
#
#         return "%s%s%s%s" % (
#             response_line,
#             response_headers,
#             blank_line,
#             response_body
#         )
#
#     def response_line(self, status_code):
#         """Returns response line"""
#         reason = self.status_codes[status_code]
#         return "HTTP/1.1 %s %s\r\n" % (status_code, reason)
#
#     def response_headers(self, extra_headers=None):
#         """Returns headers
#         The `extra_headers` can be a dict for sending
#         extra headers for the current response
#         """
#         headers_copy = self.headers.copy()  # make a local copy of headers
#
#         if extra_headers:
#             headers_copy.update(extra_headers)
#
#         headers = ""
#
#         for h in self.headers:
#             headers += "%s: %s\r\n" % (h, self.headers[h])
#         return headers
#
#     def handle_GET(self, request):
#         filename = request.uri.strip('/') #pull that slash out of the uri
#
#         if os.path.exists(filename):
#             response_line = self.response_line(200)
#
#             response_header = self.response_headers()
#
#             with open(filename) as f:
#                 response_body = f.read()
#         else:
#             response_line = self.response_line(404)
#             response_headers = self.response_headers()
#             response_body = "<h1>404 Not Found</h1>"
#
#         blank_line = "\r\n"
#
#         return "%s%s%s%s" % (
#             response_line,
#             response_headers,
#             blank_line,
#             response_body
#         )
#
#     def handle_POST(self, request):
#         #write you soon too
#         pass
#
# class HTTPRequest:
#     def __init__(self, data):
#         self.method = None
#         self.uri = None
#         self.http_version = '1.1'  # default to HTTP/1.1 if request doesn't provide a version
#         self.headers = {}  # a dictionary for headers
#
#         # call self.parse method to parse the request data
#         self.parse(data)
#
#     def parse(self, data):
#         lines = data.split('\r\n')
#
#         requests_line = lines[0]
#         self.parse_request_line(requests_line)
#
#     def parse_request_line(self, request_line):
#         words = request_line.split(' ')
#         self.method = words[0]
#         self.uri = words[1]
#
#         if len(words) > 2:
#             self.http_version = words[2]
#
#
#


#
# file = open("game.txt", "w")
# HOST = sys.argv[1]
# newgame = ['Rock', 'Paper', 'Scissors']
# class requestHandler(BaseHTTPRequestHandler):
#     def do_GET(self):
#         if self.path.endswith(''):
#             self.send_response(200)
#             self.send_header('content-type', 'text/html')
#             self.end_headers()
#
#
#
#             self.wfile.write(output.encode())
#
#     def do_POST(self):
#         if self.path.endswith(''):
#             ctype, pdict = cgi.parse_header(self.headers.get('content-type'))
#             pdict['boundary'] = bytes(pdict['boundary'], "utf-8")
#             content_len = int(self.headers.get('Content-length'))
#             pdict['CONTENT-LENGTH'] = content_len
#             if ctype == 'multipart/form-data':
#                 fields = cgi.parse_multipart(self.rfile, pdict)
#                 new_task = fields.get('move')
#                 newgame.append(new_task[0])
#                 file.write(new_task[0])
#                 file.close()
#             self.send_response(301)
#             self.send_header('content-type', 'text/html')
#             self.send_header('Location', '/newgame')
#             self.end_headers()
#
#
# def main():
#     PORT = int(sys.argv[2])
#     server = HTTPServer((HOST, PORT), requestHandler)
#     print('Server running on port %s' % PORT)
#     server.serve_forever()
#
#
# if __name__ == '__main__':
#     main()
