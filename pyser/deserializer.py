def deserializer(inp):
    hex_list = ("{:02x}".format(ord(c)) for c in inp)
    last, s = '', ''
    key_val, d = [None]*2, {}
    while True:
        try:
            n = next(hex_list)
        except StopIteration:
            break
        else:
            if n not in ['00','01','02','03','04','05']:
                byte_value = bytes.fromhex(n)
                value = byte_value.decode("utf-8")
                s += value
            elif n == '00':
                if last not in ['00','01','02','03','04','05']:
                    if key_val[0] is None:
                        key_val[0] = s
                    else:
                        key_val[1] = s
                    s = ''
                elif last in ['01','02', '03','04','05']: # when it is delimiter after value_type
                    if key_val[1] is None:
                        if last == '01':
                            key_val[0] = int(key_val[0])
                        elif last == '02':
                            key_val[0] = float(key_val[0])
                        elif last == '04':
                            key_val[0] = bool(key_val[0])
                        elif last == '05':
                            key_val[0] = complex(key_val[0])
                    else:
                        if last == '01':
                            key_val[1] = int(key_val[1])
                        elif last == '02':
                            key_val[1] = float(key_val[1])
                        elif last == '04':
                            key_val[1] = bool(key_val[1])
                        elif last == '05':
                            key_val[1] = complex(key_val[1])
                        d[key_val[0]] = key_val[1]
                        key_val = [None]*2
            last = n
    return d