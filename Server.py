import cgi
import sys
from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.request


# main.py
import socket

class TCPServer:
    def __init__(self):
        self.host = sys.argv[1]  # address for our server
        self.port = int(sys.argv[2]) # port for our server



    def start(self):
        # create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # bind the socket object to the address and port
        s.bind((self.host, self.port))
        # start listening for connections
        s.listen(5)

        print("Listening at", s.getsockname())

        while True:
            # accept any new connection
            conn, addr = s.accept()

            print("Connected by", addr)

            # read the data sent by the client (1024 bytes)
            data = conn.recv(1024)

            response = self.handle_request(data)

            # send back the data to client
            conn.sendall(data)

            # close the connection
            conn.close()

def handle_request(self, data):



class HTTPServer(TCPServer):

    status_codes = {
        200: 'OK',
        404: 'Not Found',
        501: 'Not Implemented',
    }

    def handle_request(self, data):
        # create an instance of `HTTPRequest`
        request = HTTPRequest(data)

        # now, look at the request method and call the
        # appropriate handler
        try:
            handler = getattr(self, 'handle_%s' % request.method)
        except AttributeError:
            handler = self.HTTP_501_handler

        response = handler(request)

        return response

    def HTTP_501_handler(self, request):
        response_line = self.response_line(status_code=501)

        response_headers = self.response_headers()

        blank_line = "\r\n"

        response_body = "<h1>501 Not Implemented</h1>"

        return "%s%s%s%s" % (
            response_line,
            response_headers,
            blank_line,
            response_body
        )

    def response_line(self, status_code):
        """Returns response line"""
        reason = self.status_codes[status_code]
        return "HTTP/1.1 %s %s\r\n" % (status_code, reason)

    def response_headers(self, extra_headers=None):
        """Returns headers
        The `extra_headers` can be a dict for sending
        extra headers for the current response
        """
        headers_copy = self.headers.copy()  # make a local copy of headers

        if extra_headers:
            headers_copy.update(extra_headers)

        headers = ""

        for h in self.headers:
            headers += "%s: %s\r\n" % (h, self.headers[h])
        return headers

    def handle_request(self, data):

        request = HTTPRequest(data)

        handler = getattr(self, 'handle_%s' % request.method)

        response = handler(request)

        return response

    def handle_GET(self, request):
        #write soon
        pass

    def handle_POST(self, request):
        #write you soon too
        pass

class HTTPRequest:
    def __init__(self, data):
        self.method = None
        self.uri = None
        self.http_version = '1.1'  # default to HTTP/1.1 if request doesn't provide a version
        self.headers = {}  # a dictionary for headers

        # call self.parse method to parse the request data
        self.parse(data)

    def parse(self, data):
        lines= data.split('\r\n')

        requests_line = lines[0]
        self.parse_request_line(requests_line)

    def parse_request_line(self, request_line):
        words = request_line.split(' ')
        self.method = words[0]
        self.uri = words[1]

        if len(words) > 2:
            self.http_version = words[2]





if __name__ == '__main__':
    server = HTTPServer()
    server.start()



#CITE YOUR SOURCES

# I leaned heavily on this guys guide to building an HTTP server. He walked me through everything and I got most of the code here from him.
# I modifed things to work on the ROCK, PAPER, SCICCORS methods and needs for class.
#https://bhch.github.io/posts/2017/11/writing-an-http-server-from-scratch/












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