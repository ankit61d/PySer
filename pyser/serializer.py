# NUL byte \x00 is the delimiter used, raise Error if it is present in the dictionary

delimiter = '\x00'

def get_type(inp):
    if isinstance(inp, bool): # isinstance(True, int) returns True
        return '\x04'
    elif isinstance(inp, str):
        return '\x03'
    elif isinstance(inp, int):
        return '\x01'
    elif isinstance(inp, float): #when instance is float
        return '\x02'
    elif isinstance(inp, complex):
        return '\x05'


def serializer(d):
    bytes_string = ''
    keys = list(d.keys())
    for k in keys:
        key_type = get_type(k) 
        val, val_type = d[k], get_type(d[k])
        bytes_string += str(k) + delimiter + key_type + delimiter + str(val) + delimiter + val_type + delimiter
    return bytes_string
