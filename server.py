from os import stat
from socket import socket, AF_INET, SOCK_STREAM
import sys
import json
import os

class Server():

    def __init__(self, adres = '', port = 7777):
        self.adres = adres
        self.port = port
        self.client = None
        self.socket = self.inicializeSocket()
        self.loop()


    def inicializeSocket(self):
        s = socket(AF_INET, SOCK_STREAM)
        s.bind((self.adres, self.port))
        s.listen()
        return s

    def createResponse(self, status):

        if status == 200:
            response = {"alert":"OK",
                        }
        if status == 500:
            response = {
                "alert": "Error",
                "msg": "Msg doesnot added",
                }

        response["status"] = status


        response = json.dumps(response).encode("utf-8")
        print(response)
        return response

    def pushUserMessage(self, DATA):
        result = json.loads(DATA.decode(encoding="utf-8")) #Может быть ошибка
        if os.path.isfile("msg.json"):
            with open("msg.json", "r", encoding="utf-8") as f:
                OBJ = json.load(f)
                OBJ["messages"].append(result)
        else:
            OBJ = {"messages":[]}

        with open("msg.json", "w", encoding="utf-8") as f:
            json.dump(OBJ, f, indent=4)



    def sendResponse(self, client, status=200):
        self.client.send(self.createResponse(status)) #Может быть ошибка

    def sendMessages(self):
         with open("msg.json", "r", encoding="utf-8") as f:
            OBJ = json.loads(f)


    def loop(self):
        while True:
            self.client, addr = self.socket.accept()
            with open("serverlog.log", "a+", encoding="utf-8") as f:
                f.write(f"Получен запрос на соединение от {str(addr)} \n" )

            DATA = self.client.recv(4096)
            try:
                self.pushUserMessage(DATA)
                self.sendResponse(self.client)
            except json.JSONDecodeError:
                self.sendResponse(self.client, status = 500)

            self.client.close()








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
        server = Server(ip, port)
    except:
        print("Error server creation")