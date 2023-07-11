#!/usr/bin/python3
"""
This module contains a function that appends a string at the end of a text
file (UTF8) and returns the number of characters added.
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8) and returns the number
    of characters added.

    Args:
        filename (str): The name of the file to append to.
        text (str): The text to append to the file.

    Returns:
        int: The number of characters added.
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)


if __name__ == "__main__":
    nb_chars_add = append_write("file_append.txt", "This School is so cool!\n")
    print(nb_chars_add)
