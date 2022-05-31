from constants import *
from exceptions import *
from utils import *

def deserializer(input_var):
    if type(input_var) == str:

        # from our input bytes, we must create a hex generator object so we can call them one byte at a time
        # this allows deserializer to handle large input without storing it all at once in the memory
        hex_list = ("{:02x}".format(ord(c)) for c in input_var)
        serialized_dict = {}    
            
        '''For a given key-value pair, serializer makes a bytes_string as given below:
        bytes_string = key + delimiter + key_data_type + delimiter + value + delimiter + value_data_type + delimiter
        Hence a valid deserializer output must always have 4 delimiters, or 4 steps to check if input is valid.
        The 4 steps are:- get key string, get key data type, get value string & get value data type
        '''
         

        # flag to check while loop does not loop infinitely
        is_main_while_loop = True
        steps = 0
        while is_main_while_loop:
            steps = 0
            try:
                n = next(hex_list)
            except StopIteration:
                is_main_while_loop = False
                break

            # 1st step - get all bytes for key string and store them in key_str variable
            key_str = get_entity(hex_list, n)
            # 1st step - get key string successful
            steps += 1 # steps is 1

            # 2nd step - get key data type from next(n)
            try:
                n = next(hex_list)
            except StopIteration:
                is_main_while_loop = False
                break
            # 2nd step - get key data type successful
            steps += 1 # steps is 2

            try:
                key_data_type = HEX_TO_DATA_TYPE_MAP[n]
            except KeyError:
                raise DeserializerInvalidInputError
            key = key_data_type(key_str)

            # we goto next(n) as there is delimiter after key data type
            try:
                n = next(hex_list)
            except StopIteration:
                is_main_while_loop = False
                break
            
            try:
                n = next(hex_list)
            except StopIteration:
                is_main_while_loop = False
                break
            
            value_str = get_entity(hex_list, n)
            # 3rd step - get value string successful
            steps += 1 # steps is 3

            try:
                n = next(hex_list)
            except StopIteration:
                is_main_while_loop = False
                break
            #4th step - get value data type successful
            steps += 1 # steps is 4

            try:
                value_data_type = HEX_TO_DATA_TYPE_MAP[n]
            except KeyError:
                raise DeserializerInvalidInputError

            value = value_data_type(value_str)

            # we goto next(n) as there is delimiter after value data type
            try:
                n = next(hex_list)
            except StopIteration:
                is_main_while_loop = False
                break
            
            # when all 4 steps are complete, we commit the key value pair to dictionary
            serialized_dict[key] = value

        if steps != 4:
            return serialized_dict
        else:
            '''To get a key-value pair , Serializer function must always perform 4 steps
            We increment steps everytime those steps are performed successfully 
            So, if steps != 4, it means we failed to get a key-value pair
            In other words, Deserializer Input was not a valid serializer output
            '''
            raise DeserializerInvalidInputError
    else:
        raise DeserializerInvalidInputError