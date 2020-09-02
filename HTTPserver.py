from http.server import HTTPServer, BaseHTTPRequestHandler

newgame = ['Rock', 'Paper', 'Scissors']
class echoHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.endswith('/newgame'):
            self.send_response(200)
            self.send_header('content-type', 'text/html')
            self.end_headers()

            output = ''
            output += '<html><body>'
            output += '<h1> Rock, Paper, Scissors</h1>'
            output += '<h3><a href="/newgame/new"> Start New Game</a></h3>'
            for game in newgame:
                output += game
                output += '</br>'
            output += '</body></html>'

        if self.path.endswith('/newgame'):
            self.send_response(200)
            self.send_header('content-type', 'text/html')
            self.end_headers()

            output += ''
            output += '<html><body>'
            output += '<h1> Enter your play</h1>'
            output += '<form method="POST" enctype="multipart/form-data" action=/newgame/new">'
            output += '<input name="move" type="text" placeholder="Enter move">'
            output += '<input type="submit" value="add">'
            output += '</form>'
            output += '</body>'

            self.wfile.write(output.encode())


        # self.send_response(200)
        # self.send_header('content-type', 'text/html')
        # self.end_headers()
        # self.wfile.write(self.path[1:].encode())


def main():
    PORT = 8000
    server = HTTPServer(('', PORT), echoHandler)
    print('Server running on port %s' % PORT)
    server.serve_forever()


if __name__ == '__main__':
    main()