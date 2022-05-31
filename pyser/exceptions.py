# Exception handling classes for SERIALIZER

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

# Exception handling classes for DESERIALIZER

class DeserializerInvalidInputError(Exception):
    '''Error: input is not a valid serializer output
    '''
    pass