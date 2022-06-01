import unittest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(".", "..", "../pyser")))
from serializer import serializer 
from exceptions import *

class TestSerializer(unittest.TestCase):

    # DATATYPE tests
    def test_serializer_int(self):
        self.assertEqual(serializer({12:34,-1:-2,-328476234:0 }), '12\x00\x01\x0034\x00\x01\x00-1\x00\x01\x00-2\x00\x01\x00-328476234\x00\x01\x000\x00\x01\x00')

    def test_serializer_float(self):
        self.assertEqual(serializer({1.22:5.33, -9.9:0,0:-5050.0}), '1.22\x00\x02\x005.33\x00\x02\x00-9.9\x00\x02\x000\x00\x01\x000\x00\x01\x00-5050.0\x00\x02\x00')

    def test_serializer_complex(self):
        self.assertEqual(serializer({1+2j:50,1-2j:0,1.1+2j:"50" }), '(1+2j)\x00\x05\x0050\x00\x01\x00(1-2j)\x00\x05\x000\x00\x01\x00(1.1+2j)\x00\x05\x0050\x00\x03\x00')

    def test_serializer_bool(self):
        self.assertEqual(serializer({"status":True, False:True, True:1}), 'status\x00\x03\x00True\x00\x04\x00False\x00\x04\x00True\x00\x04\x00True\x00\x04\x001\x00\x01\x00')

    def test_serializer_str(self):
        self.assertEqual(serializer({"mYsTriNG":"?", "x1-?x":123, 7.89:"ggw[", " ":" "}), 'mYsTriNG\x00\x03\x00?\x00\x03\x00x1-?x\x00\x03\x00123\x00\x01\x007.89\x00\x02\x00ggw[\x00\x03\x00 \x00\x03\x00 \x00\x03\x00')

    # TESTS TO CHECK ERROR HANDLING
    def test_serializer_type_error(self):
        self.assertRaises(SerializerTypeError, serializer,{"key":["list","Value"]})
        self.assertRaises(SerializerTypeError, serializer,{(1, "key"):"tuplekey"})
        self.assertRaises(SerializerTypeError, serializer,{"set_val":{"list","Value"}})

    def test_serializer_invalid_input(self):
        self.assertRaises(SerializerInvalidInputError, serializer,"string_input")
        self.assertRaises(SerializerInvalidInputError, serializer, [1,2,"list_input"])
        self.assertRaises(SerializerInvalidInputError, serializer, {"set","input"})
        self.assertRaises(SerializerInvalidInputError, serializer, 786)
        self.assertRaises(SerializerInvalidInputError, serializer, 1-2j)
        self.assertRaises(SerializerInvalidInputError, serializer, ("tuple", "input"))

    def test_serializer_empty_dict_error(self):
        self.assertRaises(SerializerEmptyDictError, serializer, {})

    # TESTS TO CHECK ESCAPE CHAR HANDLING FOR OPCODES
    def test_serializer_escape_char(self):
        self.assertEqual(serializer({"\x06\x00\x06":"\x00\x02\x04"}), '\x06\x06\x06\x00\x06\x06\x00\x03\x00\x06\x00\x06\x02\x06\x04\x00\x03\x00')

if __name__ == '__main__':
    unittest.main()