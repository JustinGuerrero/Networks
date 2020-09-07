import socket
import sys
import http.client
import http.server
BUFFER_SIZE = 1024
file = open("newFile.txt", "w")
host = sys.argv[1]
port = int(sys.argv[2])
class Connect():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(1)



    conn, addr = s.accept()
    data = conn.recv(BUFFER_SIZE)
    conn.send(data) #echo
    print(data)
    print(BUFFER_SIZE)
    newData = data.decode('utf-8')
    file.write(newData)
    file.close()
    #conn.close()

class main():
    Connect()