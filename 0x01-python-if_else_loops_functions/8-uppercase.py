#!/usr/bin/python3

def uppercase(str):
    for i in str:
        code = ord(i)
        if code >= 97 and code <= 122:
            code -= 32
        print("{}".format(chr(code)), end="")
print()
