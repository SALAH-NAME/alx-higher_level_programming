#!/usr/bin/python3
for alf in range(122, 96, -1):
    if alf % 2 != 0:
        char = alf - 32
    else:
        char = alf
    print("{}".format(chr(char)), end='')
