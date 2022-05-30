# NUL byte \x00 is the delimiter used, raise Error if it is present in the dictionary

delimiter = '\x00'

error_messages = {
    'InvalidInput': 'serializer takes only dict as input',
    'dictError' : 'Unsupported Key or Value Error'
}

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
    else: # when any key or value is none of these types
        return error_messages['dictError']


def serializer(d):
    '''this function takes dict as input as traverse through its key-value pairs.
    it appends key, delimiter, key_type, delimiter to bytes_string
    then in same way, for that key it appends corresponding value, delimiter, value_type and delimiter
    '''
    if isinstance(d, dict):
        bytes_string = ''
        keys = list(d.keys())
        for k in keys:
            key_type = get_type(k)
            val, val_type = d[k], get_type(d[k])
            if key_type == error_messages['dictError']  or val_type == error_messages['dictError']:
                return error_messages['dictError']
                
            else:
                bytes_string += str(k) + delimiter + key_type + delimiter + str(val) + delimiter + val_type + delimiter
                return bytes_string
    else:
        return error_messages['InvalidInput']