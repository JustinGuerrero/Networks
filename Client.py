import socket as s

HOST = '127.0.0.1'
PORT = 8080


with s.socket(s.AF_INET, s.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)


