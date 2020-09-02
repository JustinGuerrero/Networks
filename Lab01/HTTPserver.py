import sys
from http.server import HTTPServer, BaseHTTPRequestHandler

newgame = ['Rock', 'Paper', 'Scissors']
class echoHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.endswith('/'):
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



            # output += ''
            # output += '<html><body>'
            # output += '<h1> Enter your play</h1>'
            # output += '<form method="POST" enctype="multipart/form-data" action=/newgame/new">'
            # output += '<input name="move" type="text" placeholder="Enter move">'
            # output += '<input type="submit" value="add">'
            # output += '</form>'
            # output += '</body>'

            self.wfile.write(output.encode())




def main():
    PORT = 8000
    server = HTTPServer((sys.argv[1], PORT), echoHandler)
    print('Server running on port %s' % PORT)
    server.serve_forever()


if __name__ == '__main__':
    main()