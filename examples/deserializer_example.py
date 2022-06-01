import os
import sys

sys.path.append(os.path.abspath(os.path.join(".", "../pyser")))
from deserializer import deserializer

#Lazy Method for Reading Big File in Python
def read_in_chunks(file_object, chunk_size=1):
    '''Lazy function (generator) to read a file piece by piece.
    '''
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data

f = open("sample.txt","r")
#print(read_in_chunks(f))
print(deserializer(read_in_chunks(f)))