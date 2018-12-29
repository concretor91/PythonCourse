import unittest
import sys 
import os
sys.path.append(os.path.abspath('.\Homework4'))
from client_server import *

class Test_client_server(unittest.TestCase):
    def testMsgDecode(self):
        self.assertEqual(type(ReceiveMsg()), type(b''))

if __name__ == "__main__":
    unittest.main()