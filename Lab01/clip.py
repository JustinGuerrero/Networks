import socket
import sys
import http.client
import requests

BUFFER_SIZE = 1024
host = sys.argv[1]
port = int(sys.argv[2])
string = 'http://'+host+':'+sys.argv[2]
print("Put some stupid thing here")
answer = input()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

s.send(bytes(answer, 'utf-8'))
data = s.recv(BUFFER_SIZE)
data2 = data.decode('utf-8')
print(data2)
s.close()