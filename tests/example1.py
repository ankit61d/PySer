my_dict = {
    "repo": "PYSER",
    "version": 1.0,
    "is_working": True,
    "description": "Python library to (de)serialize dict to disk",
    "publish_date": "30 May 2022"
}
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
    for each in keys:
        key, key_type = each, get_type(each) 
        val, val_type = d[each], get_type(d[each])
        bytes_string += str(key) + delimiter + key_type + delimiter + str(val) + delimiter + val_type + delimiter
    return bytes_string

encoded = serializer(my_dict)
f = open("sample.txt", "w")
f. write(encoded)
f. close()
