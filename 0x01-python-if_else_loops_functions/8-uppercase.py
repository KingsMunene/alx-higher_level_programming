#!/usr/bin/python3

def uppercase(str):
    for i in range(len(str)):
        code = ord(str[i])
        if (code > 98) and (code < 123):
            code = code - 32
        print("{}".format(chr(code)), end="")
    print()
