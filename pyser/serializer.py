# NUL byte \x00 is the delimiter used, raise Error if it is present in the dictionary

delimiter = '\x00'

class SerializerInvalidInputError(Exception):
    '''Error: serializer takes only dict as input
    '''
    pass

class SerializerTypeError(Exception):
    '''Error: key or value type is not supported
    '''
    pass
class SerializerEmptyDictError(Exception):
    '''Error: serializer doesn't take empty dict as input
    '''
    pass

def get_type(inp):
    '''get_type takes input and returns the hex value mapped for that input type
    '''
    # We must check for bool first as bool is subclass of int
    if isinstance(inp, bool):
        return '\x04'
    elif isinstance(inp, float):
        return '\x02'
    elif isinstance(inp, str):
        return '\x03'
    elif isinstance(inp, int):
        return '\x01'
    elif isinstance(inp, complex):
        return '\x05'
    else: # when key or val type is not supported
        raise SerializerTypeError


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
                bytes_string += str(k) + delimiter + key_type + delimiter + str(val) + delimiter + val_type + delimiter
                return bytes_string
        else: # raise error when empty dict is passed
            raise SerializerEmptyDictError
    else: # raise error when input is other than dict
        raise SerializerInvalidInputError