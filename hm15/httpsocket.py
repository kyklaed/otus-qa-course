import socket
# import requests
# requests.post()

class Http:
    def __init__(self, host, port, head, body_requests=None, *args):
        self.host = str(host)
        self.port = int(port)
        self.head = head
        self.body_requests = body_requests
        self.request = [self.head, " /", " HTTP/1.1\n", "Host: {0}\n".format(str(self.host))]

        if self.body_requests != None and self.head.upper() == "POST":
            self.request[1] += ''.join(self.body_requests)
        print(self.request)
        print("args = ", args)

        for p in args:
            print(p)
            self.request.append(p)
        self.request.append('\r\n\r\n')
        self.sock = None

    def connect(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))

    def send(self):
        print(''.join(self.request))
        self.sock.send(''.join(self.request).encode())

    def print(self):
        data = self.sock.recv(4096)
        for i in data.decode('utf-8').split('\r\n'):
            print(i)

    def close(self):
        self.sock.close()


http = Http('192.168.88.242', 80, 'POST',
            'admin/username=admin&password=admin',
            "User-Agent: Mozilla/5.0",)
http.connect()
http.send()
http.print()
http.close()
