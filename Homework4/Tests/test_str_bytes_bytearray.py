import unittest
import sys 
import os
sys.path.append(os.path.abspath('.\Homework4'))
from str_bytes_bytearray import *

class Test_time_server(unittest.TestCase):
    def test1_DecodeByteToStr(self):
        self.assertEqual(DecodeByteToStr(b'test', 'cp1251'), 'test')

    def test2_DecodeByteToStr(self):
        with self.assertRaises(LookupError):
            DecodeByteToStr(b'test', 'cp125555')

    def test1_EncodeStrToBytes(self):
        self.assertEqual(EncodeStrToBytes('тест', 'cp1251'), b'\xf2\xe5\xf1\xf2')

    def test2_EncodeStrToBytes(self):
        self.assertEqual(EncodeStrToBytes('test', 'cp1251'), b'test')

    def test3_EncodeStrToBytes(self):
        with self.assertRaises(LookupError):
            EncodeStrToBytes('тест', 'cp1251656')

    def test1_StrToBytearrray(self):
        self.assertEqual(StrToBytearrray('test', 'utf-8'), bytearray(b'test'))

    def test2_StrToBytearrray(self):
        with self.assertRaises(TypeError):
            StrToBytearrray(b'test', 'utf-8')

if __name__ == "__main__":
    unittest.main()