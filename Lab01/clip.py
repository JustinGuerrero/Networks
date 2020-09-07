import socket
import sys
import http.client
import http.server

BUFFER_SIZE = 1024
host = sys.argv[1]
port = int(sys.argv[2])
print("Put some stupid thing here")
answer = input()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))
s.send(bytes(answer, 'utf-8'))
data = s.recv(BUFFER_SIZE)
print(data)
s.close()