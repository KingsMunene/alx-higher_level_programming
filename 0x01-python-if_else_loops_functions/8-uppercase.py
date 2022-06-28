#!/usr/bin/python3

def uppercase(str):
    tmp = list(str)
    for i in tmp:
        if (ord(i) > 96) and (ord(i) < 123):
            tmp[i] = chr(ord(tmp[i]) - 32)
    print("{}".format("".join(tmp)))
