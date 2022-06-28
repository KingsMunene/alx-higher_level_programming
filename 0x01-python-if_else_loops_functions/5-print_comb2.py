#!/usr/bin/python3
numberRange = range(0, 100)
i = 0

while i < 100:
    if i == 99:
        print("{}".format(numberRange[i]))
    else:
        print("{:02}, ".format(numberRange[i]), end="")
    i += 1
