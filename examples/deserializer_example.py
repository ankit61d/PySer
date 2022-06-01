import os
import sys

sys.path.append(os.path.abspath(os.path.join(".", "../pyser")))
from deserializer import deserializer

f = open("sample.txt","r")
#print(f.read())
print(deserializer(f))