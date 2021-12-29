import json
from socket import *
import sys


class Client():
    def __init__(self, ip="localhost", port=7777):
        self.ip = ip
        self.port = port
        self.socket = socket(AF_INET, SOCK_STREAM)
        self.socket.connect((ip, port))

    def sendMessage(self, msg):
        MSG = json.dumps({"msg": str(msg)})
        self.socket.send(MSG.encode("utf-8"))

    def recMessage(self):
        DATA = self.socket.recv(4096)
        return json.loads(DATA.decode("utf-8"))

    def closeConnection(self):
        self.socket.close()


if __name__ == "__main__":
    try:
        ip = sys.argv[1]
    except IndexError:
        ip = "localhost"
    try:
        port = int(sys.argv[2])
    except IndexError:
        port = 7777

    try:
        cli = Client(ip, port)
    except ConnectionRefusedError:
        print("Error config")
        exit()
    cli.sendMessage("Testing")
    print(cli.recMessage())
    cli.closeConnection()