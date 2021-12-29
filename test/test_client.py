import json
import unittest
import subprocess
import time
import json
import sys
import os

sys.path.append(os.path.join(os.getcwd(), '..'))
sys.path.append(os.getcwd())
from project.client import Client


class TestClient(unittest.TestCase):
    def __init__(self, methodName):
        super().__init__(methodName=methodName)

        self.spr = None
        self.client = None
        self.msgBackup = None

    def setUp(self):
        """
        Backup msg.json
        Starting server and creating client
        """
        with open("../project/msg.json", "r", encoding="utf-8") as f:
            self.msgBackup = json.load(f)

        self.spr = subprocess.Popen(["python", "../project/server.py"])
        time.sleep(1)
        self.client = Client()
        return super().setUp()

    def tearDown(self):

        self.client.closeConnection()
        self.spr.kill()
        try:
            os.remove("msg.json")
        except:
            pass
        try:
            os.remove("serverlog.log")
        except:
            pass
        with open("../project/msg.json", "w", encoding="utf-8") as f:
            json.dump(self.msgBackup, f, indent=4)

        return super().tearDown()

    def send_msg(self, msg):
        self.client.sendMessage(msg)
        self.client.recMessage()
        with open("../project/msg.json", "r", encoding="utf-8") as f:
            OBJ = json.load(f)
        self.assertEqual(OBJ["messages"][-1]["msg"], str(msg))

    def test_send_msg(self):
        msg = time.perf_counter()
        self.send_msg(msg)

    def test_send_empty_msg(self):
        msg = None
        self.send_msg(msg)

    def test_number_msg(self):
        msg = 123
        self.send_msg(msg)

    def test_send_no_msg(self):
        self.assertRaises(TypeError, self.client.sendMessage)

    def test_send_dict(self):
        msg = {"msg": 123}
        self.send_msg(msg)

    def test_send_list(self):
        msg = [123, 345, "message"]
        self.send_msg(msg)

    def test_rec_msg(self):
        self.client.sendMessage("Test")
        res = self.client.recMessage()
        self.assertEqual(res, {'alert': 'OK', 'status': 200})

    def test_rec_dict(self):
        self.client.sendMessage({"msg": "Test"})
        res = self.client.recMessage()
        self.assertEqual(res, {'alert': 'OK', 'status': 200})