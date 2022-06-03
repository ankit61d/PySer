import unittest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(".", "..", "../pyser")))
from deserializer import deserializer


class TestDeserializer(unittest.TestCase):

    # TESTS TO CHECK DATATYPES HANDLING
    def test_deserializer(self):
        self.assertEqual(deserializer('my_sTRiNG\x00\x03\x00?\x00\x03\x00'), {'my_sTRiNG':"?"})
        self.assertEqual(deserializer('1238719283721837\x00\x05\x00hello\x00\x03\x00'), {(1238719283721837+0j): "hello"})
        self.assertEqual(deserializer('-90.90\x00\x03\x001a1\x00\x03\x00'), {"-90.90":"1a1"})


    # TESTS TO CHECK ESCAPE CHAR HANDLING
    def test_deserializer_escape_char(self):
        self.assertEqual(deserializer('\x06\x06\x06\x00\x06\x06\x00\x03\x00\x06\x00\x06\x02\x06\x04\x00\x03\x00'), {"\x06\x00\x06":"\x00\x02\x04"})


if __name__ == '__main__':
    unittest.main()