#!/usr/bin/python3
i = 0
alphabetRange = range(97, 123)

while i < 26:
    if alphabetRange[i] != 101 and alphabetRange[i] != 113:
        print("{}".format(chr(alphabetRange[i])), end="")
    i += 1
