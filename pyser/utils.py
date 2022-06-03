from constants import OPCODES_1, OPCODE_ESCAPE_CHAR_2, OPCODE_ESCAPE_CHAR_1, OPCODE_DELIMITER_2, OPCODE_BOOL_DATATYPE_1, OPCODE_STRING_DATATYPE_1, OPCODE_FLOAT_DATATYPE_1, OPCODE_INT_DATATYPE_1, OPCODE_COMPLEX_DATATYPE_1
from exceptions import SerializerTypeError

# utility functions for SERIALIZER

def get_type(inp):
    '''get_type takes input and returns the hex value mapped for that input type
    '''
    # We must check for bool first as bool is subclass of int
    if isinstance(inp, bool):
        return OPCODE_BOOL_DATATYPE_1
    elif isinstance(inp, float):
        return OPCODE_FLOAT_DATATYPE_1
    elif isinstance(inp, str):
        return OPCODE_STRING_DATATYPE_1
    elif isinstance(inp, int):
        return OPCODE_INT_DATATYPE_1
    elif isinstance(inp, complex):
        return OPCODE_COMPLEX_DATATYPE_1
    else: 
        # when key or val type is not supported
        raise SerializerTypeError

def get_escaped_input_str(inp_str):
    escaped_inp_str = ''
    for each in inp_str:
        if each in OPCODES_1:
            escaped_inp_str += (OPCODE_ESCAPE_CHAR_1 + each)
        else:
            escaped_inp_str += each
    return escaped_inp_str


# utility functions for DESERIALIZER

def get_entity(hex_list, n):
    '''This function keeps calling one byte at a time from hex_list until it hits a delimiter
    When it hits delimiter, it returns the entity (key or value) string.
    '''
    entity_str = ''

    #we set a flag so that we can escape our OPODES in dict input
    is_last_char_escaped = False
    
    while n != OPCODE_DELIMITER_2 or is_last_char_escaped: 
        if (not is_last_char_escaped) and n == OPCODE_ESCAPE_CHAR_2 :
            is_last_char_escaped = True
            try:
                n = next(hex_list)
            except StopIteration:
                break
            continue

        entity_str += bytes.fromhex(n).decode("utf-8")
        is_last_char_escaped = False

        try:
            n = next(hex_list)
        except StopIteration:
            break

    return entity_str