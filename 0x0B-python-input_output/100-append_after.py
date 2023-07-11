#!/usr/bin/python3
"""
This module contains a function that inserts a line of text to a file,
after each line containing a specific string.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file, after each line containing
    a specific string.
    """
    with open(filename, 'r') as f:
        lines = f.readlines()
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)


if __name__ == "__main__":
    append_after("append_after_100.txt", "Python", "\"C is fun!\"\n")
