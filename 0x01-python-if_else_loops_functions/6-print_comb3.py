#!/usr/bin/python3
i = 0
numberRange = range(0, 10)

while i < 10:
    for j in range(i + 1, 10):
        if (not (numberRange[i] == 8 and j == 9)):
            print("{}{}".format(numberRange[i], j), end=", ")
        else:
            print("{}{}".format(i, j))
    i += 1
