#!/usr/bin/python3
def remove_char_at(str, n):
    alf = ""
    for pos in range(len(str)):
        if pos != n:
            alf += str[pos]
    return (alf)
