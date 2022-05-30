try:
    from pyser import *
except ImportError:
    import os
    import sys

    sys.path.append(os.path.abspath(os.path.join(".", "..")))
    from pyser import *

my_dict = {
    "repo": "PYSER",
    "version": 1.0,
    "is_working": True,
    "description": "Python library to (de)serialize dict to disk",
    "publish_date": "30 May 2022"
}


encoded = serializer(my_dict)
f = open("sample.txt", "w")
f. write(encoded)
f. close()
