import cgi
import sys
from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.request


file = open("game.txt", "w")
HOST = sys.argv[1]
newgame = ['Rock', 'Paper', 'Scissors']
class requestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.endswith(''):
            self.send_response(200)
            self.send_header('content-type', 'text/html')
            self.end_headers()

            output = ''
            output += '<html><body>'
            output += 'Your move options are:'
            output += '<h1> Rock, Paper, Scissors</h1>'
            output += 'Please send your response... and one more thing'
            output += '<h3> GOOD LUCK BEATING ME BLAKE</h3>'
            output += "<h2>Please select a move</h2>"
            for game in newgame:
                output += game
                output += '</br>'
            output += '</body></html>'



            output += ''
            output += '<html><body>'
            output += '<h1> Enter your play</h1>'
            output += '<form method="POST" enctype="multipart/form-data" action="/newgame">'
            output += '<input name="move" type="text" placeholder="Enter move">'
            output += '<input type="submit" value="add">'
            output += '</form>'
            output += '</body>'

            self.wfile.write(output.encode())

    def do_POST(self):
        if self.path.endswith(''):
            ctype, pdict = cgi.parse_header(self.headers.get('content-type'))
            pdict['boundary'] = bytes(pdict['boundary'], "utf-8")
            content_len = int(self.headers.get('Content-length'))
            pdict['CONTENT-LENGTH'] = content_len
            if ctype == 'multipart/form-data':
                fields = cgi.parse_multipart(self.rfile, pdict)
                new_task = fields.get('move')
                newgame.append(new_task[0])
                file.write(new_task[0])
                file.close()
            self.send_response(301)
            self.send_header('content-type', 'text/html')
            self.send_header('Location', '/newgame')
            self.end_headers()


def main():
    PORT = 8000
    server = HTTPServer((HOST, PORT), requestHandler)
    print('Server running on port %s' % PORT)
    server.serve_forever()


if __name__ == '__main__':
    main()