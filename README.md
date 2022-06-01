# PySer
Simple 🐍 Python library to Serialize / Deserialize dict created for fun and educational purpose.
It uses NUL byte as a delimiter. See constants.py for other OPCODES used.

## Guide
Pyser supports primitive types in a dictionary including:
```
int
str
bool
float
complex
```
Moreover, Both serializer & deserializer can escape the OPCODES if they are present in the input.

### An example that uses pyser to serializer a dict and then deserialize it. 
1. Download the package. Navigate to the package directory in terminal & open python interpreter.
```console
ankit@slim:~/PySer$ python3
```
2. Serializer 
```console
>>> from pyser import serializer
>>> serializer({"repo":"PYSER", "watching":1, "stars":False, "floatval":5.33, 1+2j:"complexkey"})
'repo\x00\x03\x00PYSER\x00\x03\x00watching\x00\x03\x001\x00\x01\x00stars\x00\x03\x00False\x00\x04\x00floatval\x00\x03\x005.33\x00\x02\x00(1+2j)\x00\x05\x00complexkey\x00\x03\x00'
```
3. Deserializer , we copy result from serializer() command above.
```console
>>> from pyser import deserializer
>>> deserializer('repo\x00\x03\x00PYSER\x00\x03\x00watching\x00\x03\x001\x00\x01\x00stars\x00\x03\x00False\x00\x04\x00floatval\x00\x03\x005.33\x00\x02\x00(1+2j)\x00\x05\x00complexkey\x00\x03\x00')
{'repo': 'PYSER', 'watching': 1, 'stars': True, 'floatval': 5.33, (1+2j): 'complexkey'}
```

## Writing to a File
To check how pyser serializer writes dict to a file, run example1.py in examples.
It creates a file named sample.txt in the same directory.
We can hexdump this file in terminal to get idea of internal working.
### examples/serializer_example.py
```console
ankit@slim:~/PySer/examples$ python3 serializer_example.py
ankit@slim:~/PySer/examples$ hexdump -C sample.txt
00000000  72 65 70 6f 00 03 00 50  59 53 45 52 00 03 00 76  |repo...PYSER...v|
00000010  65 72 73 69 6f 6e 00 03  00 31 2e 30 00 02 00 69  |ersion...1.0...i|
00000020  73 5f 77 6f 72 6b 69 6e  67 00 03 00 54 72 75 65  |s_working...True|
00000030  00 04 00 64 65 73 63 72  69 70 74 69 6f 6e 00 03  |...description..|
00000040  00 50 79 74 68 6f 6e 20  6c 69 62 72 61 72 79 20  |.Python library |
00000050  74 6f 20 28 64 65 29 73  65 72 69 61 6c 69 7a 65  |to (de)serialize|
00000060  20 64 69 63 74 20 74 6f  20 64 69 73 6b 00 03 00  | dict to disk...|
00000070  70 75 62 6c 69 73 68 5f  64 61 74 65 00 03 00 33  |publish_date...3|
00000080  30 20 4d 61 79 20 32 30  32 32 00 03 00           |0 May 2022...|
0000008d
```

## Reading from a File
Now, we read the same sample.txt created earlier by example.
Run deserializer_example.py under examples directory. PySer deserializer reads the file and returns the original dict which was used to create sample.txt  

### examples/deserializer_example.py
```console
ankit@slim:~/PySer/examples$ python3 deserializer_example.py
{'repo': 'PYSER', 'version': 1.0, 'is_working': True, 'description': 'Python library to (de)serialize dict to disk', 'publish_date': '30 May 2022'}
```

## How to run Test cases

To run test for serializer function, navigate to tests/serializer & simply run:
```console
ankit@slim:~/PySer/tests/serializer$ python3 test.py
........
----------------------------------------------------------------------
Ran 8 tests in 0.000s

OK
```
Similarly, navigate to test/deserializer directory & run:
```console
ankit@slim:~/PySer/tests/deserializer$ python3 test.py
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```


## Improvements
This was created for fun and educational purpose. Any usage other than that is not advised.
Below are improvements which can be worked upon:
1. It does not support data types like list, tuple, set in the dict.
2. It does not support nested dict.
3. Deserializer does a better job at reading input because it uses generator to  calls bytes in memory one at a time. Serializer's ability to handle large files and save space can certainly be improved. 
