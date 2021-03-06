# -- OPCODES_1 for Serializer --
OPCODE_DELIMITER_1 = '\x00'
OPCODE_INT_DATATYPE_1 = '\x01'
OPCODE_FLOAT_DATATYPE_1 = '\x02'
OPCODE_STRING_DATATYPE_1 = '\x03'
OPCODE_BOOL_DATATYPE_1 = '\x04'
OPCODE_COMPLEX_DATATYPE_1 = '\x05'
OPCODE_ESCAPE_CHAR_1 = '\x06'

OPCODES_1 = [OPCODE_DELIMITER_1, OPCODE_INT_DATATYPE_1, OPCODE_FLOAT_DATATYPE_1, OPCODE_STRING_DATATYPE_1, OPCODE_BOOL_DATATYPE_1, OPCODE_COMPLEX_DATATYPE_1, OPCODE_ESCAPE_CHAR_1]

# -- OPCODES_2 for Deserializer -- 
OPCODE_DELIMITER_2 = '00'
OPCODE_ESCAPE_CHAR_2 = '06'

HEX_TO_DATA_TYPE_MAP = {
    '01':int,
    '02':float,
    '03':str,
    '04':bool,
    '05':complex
}