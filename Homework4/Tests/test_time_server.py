import unittest
import sys 
import os
sys.path.append(os.path.abspath('.\Homework4'))
from time_server import getTimestr
import time

class Test_time_server(unittest.TestCase):

    # def setUp(self):
    #     timestr = time.ctime(time.time()) + "\n"

    #     def tearDown(self):
    #         client_socket.close()

    def test_getTimestr1(self):
        timestr = time.ctime(time.time()) + "\n"
        self.assertNotEqual(getTimestr(), timestr)

    def test_getTimestr2(self):
        timestr = time.ctime(time.time()) + "\n"
        self.assertEqual(getTimestr(), timestr.encode('ascii'))

if __name__ == "__main__":
    unittest.main()