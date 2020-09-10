import cgi
import sys
from http.server import HTTPServer, BaseHTTPRequestHandler, SimpleHTTPRequestHandler
import http.server
import urllib.request
import os
# main.py
import pickle
import socket
from socket import *
import os
import copy
import datetime
import email.utils
import html
import http.client
import io
import mimetypes
import os
import posixpath
import select
import shutil
import socket # For gethostbyaddr()
import socketserver
import sys
import time
import urllib.parse

from functools import partial

from http import HTTPStatus

__version__ = "0.6"
filin = open("newFile1.txt", "a")


class RPShandler(SimpleHTTPRequestHandler):
    server_version = "SimpleHTTP/" + __version__

    def __init__(self, *args, directory=None, **kwargs):
        if directory is None:
            directory = os.getcwd()
        self.directory = directory
        super().__init__(*args, **kwargs)

    def do_GET(self):
        """Serve a GET request."""
        f = self.send_head()
        if f:
            try:
                self.copyfile(f, self.wfile)
            finally:
                f.close()

    def do_HEAD(self):
        """Serve a HEAD request."""
        f = self.send_head()
        if f:
            f.close()

    def do_POST(self):
        '''Serve a POST REQUEST'''
        print(self.client_address)
        print("made it to post and above is client address")
        #raw_post_data = self.rfile.read(int(self.headers['Content-Length']));
        raw_post_data = self.rfile.read(int(self.headers['Content-Length']))
        print(raw_post_data)
        data = raw_post_data.decode('utf-8')
        new = str(data)
        split_data = new.split(" ")
        print(split_data[0])
        print(split_data[1])
        with open("whos_turn_it_is.txt", "r") as who:
            turn_propper = who.read()
            if(split_data[0]!=turn_propper):
                self.send_response()








        filin.write(new)
        filin.close()
        self.send_response(200, message="WRECK")
        self.send_head()
        self.send_response(201,message="GET FUCKED YOU ORNRY BASTERED")


       # self.send_response(200, raw_post_data)




        # urlParsed_data =urllib.parse.urlparse(raw_post_data)
        #print(urlParsed_data)
        #self._determine_response(raw_post_data);


    def send_head(self):
        """Common code for GET and HEAD commands.

        This sends the response code and MIME headers.

        Return value is either a file object (which has to be copied
        to the outputfile by the caller unless the command was HEAD,
        and must be closed by the caller under all circumstances), or
        None, in which case the caller has nothing further to do.

        """
        path = self.translate_path(self.path)
        f = None
        if os.path.isdir(path):
            parts = urllib.parse.urlsplit(self.path)
            if not parts.path.endswith('/'):
                # redirect browser - doing basically what apache does
                self.send_response(HTTPStatus.MOVED_PERMANENTLY)
                new_parts = (parts[0], parts[1], parts[2] + '/',
                             parts[3], parts[4])
                new_url = urllib.parse.urlunsplit(new_parts)
                self.send_header("Location", new_url)
                self.end_headers()
                return None
            for index in "index.html", "index.htm":
                index = os.path.join(path, index)
                if os.path.exists(index):
                    path = index
                    break
            else:
                return self.list_directory(path)
        ctype = self.guess_type(path)
        try:
            f = open(path, 'rb')
        except OSError:
            self.send_error(HTTPStatus.NOT_FOUND, "File not found")
            return None

        try:
            fs = os.fstat(f.fileno())
            # Use browser cache if possible
            if ("If-Modified-Since" in self.headers
                    and "If-None-Match" not in self.headers):
                # compare If-Modified-Since and time of last file modification
                try:
                    ims = email.utils.parsedate_to_datetime(
                        self.headers["If-Modified-Since"])
                except (TypeError, IndexError, OverflowError, ValueError):
                    # ignore ill-formed values
                    pass
                else:
                    if ims.tzinfo is None:
                        # obsolete format with no timezone, cf.
                        # https://tools.ietf.org/html/rfc7231#section-7.1.1.1
                        ims = ims.replace(tzinfo=datetime.timezone.utc)
                    if ims.tzinfo is datetime.timezone.utc:
                        # compare to UTC datetime of last modification
                        last_modif = datetime.datetime.fromtimestamp(
                            fs.st_mtime, datetime.timezone.utc)
                        # remove microseconds, like in If-Modified-Since
                        last_modif = last_modif.replace(microsecond=0)

                        if last_modif <= ims:
                            self.send_response(HTTPStatus.NOT_MODIFIED)
                            self.end_headers()
                            f.close()
                            return None

            self.send_response(HTTPStatus.OK)
            self.send_header("Content-type", ctype)
            self.send_header("Content-Length", str(fs[6]))
            self.send_header("Last-Modified",
                             self.date_time_string(fs.st_mtime))
            self.end_headers()
            return f
        except:
            f.close()
            raise

    def list_directory(self, path):
        """Helper to produce a directory listing (absent index.html).

        Return value is either a file object, or None (indicating an
        error).  In either case, the headers are sent, making the
        interface the same as for send_head().

        """
        try:
            list = os.listdir(path)
        except OSError:
            self.send_error(
                HTTPStatus.NOT_FOUND,
                "No permission to list directory")
            return None
        list.sort(key=lambda a: a.lower())
        r = []
        try:
            displaypath = urllib.parse.unquote(self.path,
                                               errors='surrogatepass')
        except UnicodeDecodeError:
            displaypath = urllib.parse.unquote(path)
        displaypath = html.escape(displaypath, quote=False)
        enc = sys.getfilesystemencoding()
        title = 'Directory listing for %s' % displaypath
        r.append('<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" '
                 '"http://www.w3.org/TR/html4/strict.dtd">')
        r.append('<html>\n<head>')
        r.append('<meta http-equiv="Content-Type" '
                 'content="text/html; charset=%s">' % enc)
        r.append('<title>%s</title>\n</head>' % title)
        r.append('<body>\n<h1>%s</h1>' % title)
        r.append('<hr>\n<ul>')
        for name in list:
            fullname = os.path.join(path, name)
            displayname = linkname = name
            # Append / for directories or @ for symbolic links
            if os.path.isdir(fullname):
                displayname = name + "/"
                linkname = name + "/"
            if os.path.islink(fullname):
                displayname = name + "@"
                # Note: a link to a directory displays with @ and links with /
            r.append('<li><a href="%s">%s</a></li>'
                     % (urllib.parse.quote(linkname,
                                           errors='surrogatepass'),
                        html.escape(displayname, quote=False)))
        r.append('</ul>\n<hr>\n</body>\n</html>\n')
        encoded = '\n'.join(r).encode(enc, 'surrogateescape')
        f = io.BytesIO()
        f.write(encoded)
        f.seek(0)
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-type", "text/html; charset=%s" % enc)
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()
        return f

    def translate_path(self, path):
        """Translate a /-separated PATH to the local filename syntax.

        Components that mean special things to the local file system
        (e.g. drive or directory names) are ignored.  (XXX They should
        probably be diagnosed.)

        """
        # abandon query parameters
        path = path.split('?', 1)[0]
        path = path.split('#', 1)[0]
        # Don't forget explicit trailing slash when normalizing. Issue17324
        trailing_slash = path.rstrip().endswith('/')
        try:
            path = urllib.parse.unquote(path, errors='surrogatepass')
        except UnicodeDecodeError:
            path = urllib.parse.unquote(path)
        path = posixpath.normpath(path)
        words = path.split('/')
        words = filter(None, words)
        path = self.directory
        for word in words:
            if os.path.dirname(word) or word in (os.curdir, os.pardir):
                # Ignore components that are not a simple file/directory name
                continue
            path = os.path.join(path, word)
        if trailing_slash:
            path += '/'
        return path

    def copyfile(self, source, outputfile):
        """Copy all data between two file objects.

        The SOURCE argument is a file object open for reading
        (or anything with a read() method) and the DESTINATION
        argument is a file object open for writing (or
        anything with a write() method).

        The only reason for overriding this would be to change
        the block size or perhaps to replace newlines by CRLF
        -- note however that this the default server uses this
        to copy binary data as well.

        """
        shutil.copyfileobj(source, outputfile)

    def guess_type(self, path):
        """Guess the type of a file.

        Argument is a PATH (a filename).

        Return value is a string of the form type/subtype,
        usable for a MIME Content-type header.

        The default implementation looks the file's extension
        up in the table self.extensions_map, using application/octet-stream
        as a default; however it would be permissible (if
        slow) to look inside the data to make a better guess.

        """

        base, ext = posixpath.splitext(path)
        if ext in self.extensions_map:
            return self.extensions_map[ext]
        ext = ext.lower()
        if ext in self.extensions_map:
            return self.extensions_map[ext]
        else:
            return self.extensions_map['']

    if not mimetypes.inited:
        mimetypes.init()  # try to read system mime.types
    extensions_map = mimetypes.types_map.copy()
    extensions_map.update({
        '': 'application/octet-stream',  # Default
        '.py': 'text/plain',
        '.c': 'text/plain',
        '.h': 'text/plain',
    })


# Utilities for CGIHTTPRequestHandler

def _url_collapse_path(path):
    """
    Given a URL path, remove extra '/'s and '.' path elements and collapse
    any '..' references and returns a collapsed path.

    Implements something akin to RFC-2396 5.2 step 6 to parse relative paths.
    The utility of this function is limited to is_cgi method and helps
    preventing some security attacks.

    Returns: The reconstituted URL, which will always start with a '/'.

    Raises: IndexError if too many '..' occur within the path.

    """
    # Query component should not be involved.
    path, _, query = path.partition('?')
    path = urllib.parse.unquote(path)

    # Similar to os.path.split(os.path.normpath(path)) but specific to URL
    # path semantics rather than local operating system semantics.
    path_parts = path.split('/')
    head_parts = []
    for part in path_parts[:-1]:
        if part == '..':
            head_parts.pop()  # IndexError if more '..' than prior parts
        elif part and part != '.':
            head_parts.append(part)
    if path_parts:
        tail_part = path_parts.pop()
        if tail_part:
            if tail_part == '..':
                head_parts.pop()
                tail_part = ''
            elif tail_part == '.':
                tail_part = ''
    else:
        tail_part = ''

    if query:
        tail_part = '?'.join((tail_part, query))

    splitpath = ('/' + '/'.join(head_parts), tail_part)
    collapsed_path = "/".join(splitpath)

    return collapsed_path


nobody = None


def nobody_uid():
    """Internal routine to get nobody's uid"""
    global nobody
    if nobody:
        return nobody
    try:
        import pwd
    except ImportError:
        return -1
    try:
        nobody = pwd.getpwnam('nobody')[2]
    except KeyError:
        nobody = 1 + max(x[2] for x in pwd.getpwall())
    return nobody


def executable(path):
    """Test for executable file."""
    return os.access(path, os.X_OK)

    # def do_GET(self):
     #     print(os.getcwd())
     #     print(os.listdir())
     #     super(RPShandler, self).do_GET()


def run(server_class=HTTPServer, handler_class=RPShandler):

 server_address = (sys.argv[1], int(sys.argv[2]))
 httpd = server_class(server_address, handler_class)
 httpd.serve_forever()

 httpd.handle_request()


if __name__ == "__main__":
    run()









#CLIENT 2
#
# def switcher(argument):
#
#     switcher = {
#         1: "POST",
#         2: "GET",
#         3: "March",
#         4: "April",
#         5: "May",
#         6: "June",
#         7: "July",
#         8: "August",
#         9: "September",
#         10: "October",
#         11: "November",
#         12: "December"
#     }
#     print switcher.get(argument, "Invalid month")
#
# def createServer():
#     serversocket = socket(AF_INET, SOCK_STREAM)
#     try:
#         serversocket.bind((sys.argv[1], int(sys.argv[2])))
#         serversocket.listen(5)
#         while(1):
#
#
#             (clientsocket, address) = serversocket.accept()
#             rd= clientsocket.recv(5000).decode()
#             pieces = rd.split(" ")
#             print(pieces)
#             print(pieces[0])
#
#             if (pieces[0] == "POST"):
#                     f = open("game.txt", "a")
#                     data2 = pieces[1]
#                     f.write(data2+" ")
#                     f.close()
#                     data2 = "202 ACCEPTED " +data2 + " WRITTEN TO GAME"
#                     print(data2)
#                     clientsocket.sendall(data2.encode())
#                     clientsocket.shutdown(SHUT_WR)
#
#             elif(pieces[0] == "GET"):
#                     print("Hit GET")
#                     with open("game.txt", "r") as gamefile:
#                         data = "200 OK"
#                         data += gamefile.read()
#                         print("GAMEFILE DATA:",data)
#
#
#                     clientsocket.sendall(data.encode())
#                     clientsocket.shutdown(SHUT_WR)
#
#             elif (pieces[0] == "OPTIONS"):
#                 print("Hit OPTIONS")
#                 with open("Player_Nos.txt", "r") as playerone_file:
#                     dataoptions = playerone_file.read()
#                     print("Player DATA:", dataoptions)
#                     playerone_file.close()
#                     if(dataoptions == "0N"):
#                         with open("Player_Nos.txt", "w") as playerone_file_write:
#                             playerone_file_write.write("0")
#                             playerone_file_write.close()
#                             playerone_number = "0"
#
#
#                             clientsocket.sendall(playerone_number.encode())
#                             clientsocket.shutdown(SHUT_WR)
#                             continue
#                     with open("Player_Nos2.txt", "r") as playertwo_file:
#                         dataoptions2 = playertwo_file.read()
#                         print("Player DATA:", dataoptions2)
#                         playertwo_file.close()
#                         if (dataoptions2 == "1N"):
#                             with open("Player_Nos2.txt", "w") as playertwo_file_write:
#                                 playertwo_file_write.write("1")
#                                 playertwo_file_write.close()
#                                 playertwo_number = "1"
#                                 clientsocket.sendall(playertwo_number.encode())
#                                 clientsocket.shutdown(SHUT_WR)
#                                 continue
#
#
#
#                 # clientsocket.sendall(data.encode())
#                 # clientsocket.shutdown(SHUT_WR)
#
#             else:
#                 data = "501 NOT IMPLEMENTED"
#                 clientsocket.sendall(data.encode())
#                 clientsocket.shutdown(SHUT_WR)
#     except KeyboardInterrupt:
#             print("\nShutting down...\n");
#     # except Exception as exc:
    #         print("Error:\n");
    #         print(exc)
    #
    #  serversocket.close()




# print('Access http://localhost:9000')
# createServer()







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
#  print()

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
