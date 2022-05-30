try:
    from pyser import *
except ImportError:
    import os
    import sys

    sys.path.append(os.path.abspath(os.path.join(".", "..")))
    from pyser import *


f = open("sample.txt","r")

print(deserializer(f.read()))