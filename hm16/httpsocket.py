import socket
from html.parser import HTMLParser
from collections import Counter


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

    def get(self, lst='yes'):
        data = self.sock.recv(4096).decode('utf-8')
        if lst.lower() == 'no':
            for i in data.split('\r\n'):
                print(i)
                return 0
        elif lst.lower() == 'yes':
            start_pos = data.find("<!DOCTYPE html>")
            return data[:start_pos], data[start_pos:]
        else:
            return "Error!"

    def close(self):
        self.sock.close()


class Parser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.data = None
        self.out = {"link": [], "img": [], "tags": []}

    def handle_starttag(self, tag, attrs):
        self.out["tags"].append(tag)
        for attr in attrs:
            if attr[0] == "href":
                for pic in [".png", '.jpg']:
                    if attr[1].find(pic) != -1 and attr[1].find("http") > -1:
                        self.out["img"].append(attr[1])
                    elif attr[1].find("http") > -1:
                        self.out["link"].append(attr[1])

    def print(self, data):
        list_t = list(dict(Counter(self.out["tags"])).items())
        ans = sorted(list_t, key=lambda x: x[1], reverse=True)
        print(data.split('\r\n')[:4])
        print("popular: ", ans[:3])
        print("tags: ", self.out["tags"])
        print("link: ", self.out["link"])
        print("img: ", self.out["img"])


http = Http('192.168.88.242', 80)
http.connect()
http.send()
data = http.get()
http.close()
pars = Parser()
pars.feed(data[1])
pars.print(data[0])


