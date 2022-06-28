#!/usr/bin/python3
i = 0
numberRange = range(0, 99)
while i < 99:
    print("{} = {}".format(numberRange[i], hex(numberRange[i])))
    i += 1
