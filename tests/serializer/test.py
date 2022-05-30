import unittest

try:
    from pyser import *
except ImportError:
    import os
    import sys

    sys.path.append(os.path.abspath(os.path.join(".", "..", "..")))
    from pyser.serializer import *

class TestSerializer(unittest.TestCase):

    def test_serializer_int(self):
        self.assertEqual(serializer({12:34}), '12\x00\x01\x0034\x00\x01\x00')
        self.assertEqual(serializer({-1:-2}), '-1\x00\x01\x00-2\x00\x01\x00')
        self.assertEqual(serializer({0:0}), '0\x00\x01\x000\x00\x01\x00')
        self.assertEqual(serializer({-328476234:0}), '-328476234\x00\x01\x000\x00\x01\x00')

    def test_serializer_float(self):
        self.assertEqual(serializer({1.22:5.33}), '1.22\x00\x02\x005.33\x00\x02\x00')
        self.assertEqual(serializer({-9.9:0}), '-9.9\x00\x02\x000\x00\x01\x00')
        self.assertEqual(serializer({0:-5050.0}), '0\x00\x01\x00-5050.0\x00\x02\x00')

    def test_serializer_complex(self):
        self.assertEqual(serializer({1+2j:50}), '(1+2j)\x00\x05\x0050\x00\x01\x00')
        self.assertEqual(serializer({1-2j:0}), '(1-2j)\x00\x05\x000\x00\x01\x00')
        self.assertEqual(serializer({1.1+2j:"50"}), '(1.1+2j)\x00\x05\x0050\x00\x03\x00')

    def test_serializer_bool(self):
        self.assertEqual(serializer({"status":True}), 'status\x00\x03\x00True\x00\x04\x00')
        self.assertEqual(serializer({False:True}), 'False\x00\x04\x00True\x00\x04\x00')
        self.assertEqual(serializer({True:1}), 'True\x00\x04\x001\x00\x01\x00')

    def test_serializer_str(self):
        self.assertEqual(serializer({"mYsTriNG":"?"}), 'mYsTriNG\x00\x03\x00?\x00\x03\x00')
        self.assertEqual(serializer({"x1-?x":123}), 'x1-?x\x00\x03\x00123\x00\x01\x00')
        self.assertEqual(serializer({7.89:"ggw["}), '7.89\x00\x02\x00ggw[\x00\x03\x00')
        self.assertEqual(serializer({" ":" "}), ' \x00\x03\x00 \x00\x03\x00')

if __name__ == '__main__':
    unittest.main()