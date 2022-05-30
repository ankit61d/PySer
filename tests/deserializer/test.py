import unittest

try:
    from pyser import *
except ImportError:
    import os
    import sys
    sys.path.append(os.path.abspath(os.path.join(".", "..", "..")))
    from pyser.deserializer import *

class TestDeserializer(unittest.TestCase):

    def test_deserializer(self):
        self.assertEqual(deserializer(''), {})
        self.assertEqual(deserializer('my_sTRiNG\x00\x03\x00?\x00\x03\x00'), {'my_sTRiNG':"?"})
        self.assertEqual(deserializer('1238719283721837\x00\x05\x00hello\x00\x03\x00'), {(1238719283721837+0j): "hello"})
        self.assertEqual(deserializer('-90.90\x00\x03\x001a1\x00\x03\x00'), {"-90.90":"1a1"})
        #self.assertEqual(deserializer({}), #What this should give#) >> returns {}

    #Tests to check errors 

    def test_deserializer_type_error(self):
        # TypeError : deserializer() missing 1 required positional argument: 'input_str'
        self.assertRaises(TypeError, deserializer, )
        self.assertRaises(TypeError, deserializer, {"string", "in", "set"})

    def test_deserializer_value_error(self):    
        # should raise ValueError
        self.assertRaises(ValueError, deserializer,'1.0\x00\x01\x000\x00\x03\x00') 
        self.assertRaises(ValueError, deserializer,'True\x00\x03\x00True\x00\x01\x00')


if __name__ == '__main__':
    unittest.main()