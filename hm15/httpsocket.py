import socket


class Http:
    def __init__(self, host, port):
        self.host = str(host)
        self.port = int(port)
        self.str = ''.join(('GET / HTTP/1.1\nHost: ', str(host), '\r\n\r\n'))
        self.sock = None

    def connect(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))

    def send(self):
        self.sock.send(self.str.encode())

    def print(self):
        data = self.sock.recv(4096)
        for i in data.decode('utf-8').split('\r\n'):
            print(i)

    def close(self):
        self.sock.close()


http = Http('192.168.88.242', 80)
http.connect()
http.send()
http.print()
http.close()
