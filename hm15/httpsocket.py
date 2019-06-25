import socket
import json


class Http:
    def __init__(self, host, port, head, *args):
        self.host = str(host)
        self.port = int(port)
        self.head = head
        self.request = ["{0} / HTTP/1.1\n".format(self.head),
                        "Host: {0}\n".format(str(host))
                        ]
        for p in args:
            self.request.append(p)
        self.request.append('\r\n\r\n')
        self.sock = None

    def connect(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))

    def send(self):
        self.sock.send(''.join(self.request).encode())

    def print(self):
        data = self.sock.recv(4096)
        for i in data.decode('utf-8').split('\r\n'):
            print(i)

    def close(self):
        self.sock.close()


http = Http('192.168.88.242', 80, 'GET',
            "User-Agent: Mozilla/5.0")
http.connect()
http.send()
http.print()
http.close()
