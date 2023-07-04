#!/usr/bin/python3
"""Module for LockedClass"""


class LockedClass:
    """A class with no class or object attribute, that prevents the user from
    dynamically creating new instance attributes, except if the new instance
    attribute is called first_name.
    """
    __slots__ = ['first_name']

    def __init__(self):
        """Initializes a new LockedClass object"""
        pass
