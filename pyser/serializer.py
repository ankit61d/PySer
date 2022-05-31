from constants import *
from exceptions import *
from utils import *

# NUL byte \x00 is the delimiter used, raise Error if it is present in the dictionary

def serializer(d):
    '''this function takes dict as input as traverse through its key-value pairs.
    it appends key, delimiter, key_type, delimiter to bytes_string
    then in same way, for that key it appends corresponding value, delimiter, value_type and delimiter
    '''
    if isinstance(d, dict):
        if len(d) != 0:
            bytes_string = ''
            keys = list(d.keys())

            for k in keys:
                key_type = get_type(k)
                val, val_type = d[k], get_type(d[k])
                
                if key_type == OPCODE_STRING_DATATYPE_1:
                    bytes_string += (get_escaped_input_str(k) + OPCODE_DELIMITER_1 + key_type + OPCODE_DELIMITER_1)
                else:
                    bytes_string += str(k) + OPCODE_DELIMITER_1 + key_type + OPCODE_DELIMITER_1
                
                if val_type == OPCODE_STRING_DATATYPE_1:
                    bytes_string += (get_escaped_input_str(val) + OPCODE_DELIMITER_1 + val_type + OPCODE_DELIMITER_1)
                else:
                    bytes_string += str(val) + OPCODE_DELIMITER_1 + val_type + OPCODE_DELIMITER_1
            
            return bytes_string
        else: 
            # raise error when empty dict is passed
            raise SerializerEmptyDictError
    else: 
        # raise error when input is other than dict
        raise SerializerInvalidInputError