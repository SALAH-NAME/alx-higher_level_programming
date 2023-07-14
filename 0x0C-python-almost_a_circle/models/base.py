#!/usr/bin/python3
"""Defines the Base class for the project"""


class Base:
    """Base class for the project"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base instance

        Args:
            id (int): The id of the new Base instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
