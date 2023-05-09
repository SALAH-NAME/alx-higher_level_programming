#!/usr/bin/python3
islower = __import__('7-islower').islower


def uppercase(str):
    upstr = ''
    for ch in str:
        if islower(ch):
            upstr += chr(ord(ch) - 32)
        else:
            upstr += ch
    print("{}".format(upstr))
