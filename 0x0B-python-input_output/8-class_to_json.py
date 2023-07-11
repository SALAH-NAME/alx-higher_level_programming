#!/usr/bin/python3
"""Module containing a function that returns the dictionary description
with simple data structure (list, dictionary, string, integer and boolean)
for JSON serialization of an object.
"""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure

    Args:
        obj: An instance of a class.

    Returns:
        The dictionary description of obj.
    """
    return obj.__dict__
