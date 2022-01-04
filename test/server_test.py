import json
import unittest
import subprocess
import time
import json
import random
import sys
import os
import threading
sys.path.append(os.path.join(os.getcwd(), '..'))
sys.path.append(os.getcwd())
print(sys.path)
from project.server import Server


class TestServer(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        self.server = Server('', random.randint(81, 9000))
        self.th = threading.Thread(target=self.server.loop)
        self.th.start()
        super().__init__(methodName=methodName)

    def test_correct_message(self):
        msg = "Test Server"
        self.server.pushUserMessage({"msg":msg})

    #     with open("msg.json", "r", encoding="utf-8") as f:
    #         OBJ = json.load(f)

    #     self.assertEqual(OBJ["messages"][-1]["msg"], msg)

    def test_incorrect_message(self):

        msg = "Test Server"
        self.server.pushUserMessage(msg)


if __name__ == "__main__":
    pass