import socket
import sys
import http.server
BUFFER_SIZE = 1024

host = sys.argv[1]
port = int(sys.argv[2])
class Connect():
    def socketStuff(self):
        while(1):
            file = open("newFile.txt", "a")
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.bind((host, port))
            s.listen(1)
            conn, addr = s.accept()
            data = conn.recv(BUFFER_SIZE)
            conn.send(data) #echo
            print(data)
            print(BUFFER_SIZE)
            newData = data.decode('utf-8')
            file.write(newData + '\n')
            file.close()
        conn.close()
    # def do_get(self):
    #     self.
class main():
    Connect().socketStuff()