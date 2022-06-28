#!/usr/bin/python3
i = 0
# The range of lowcase alphabets to be looped through
alphabetRange = range(97, 123)
while i < 26:
    # print the alphabet at a given number in the range
    # use chr to convert the int to a character
    print("{}".format(chr(alphabetRange[i])), end="")
    i = i + 1
