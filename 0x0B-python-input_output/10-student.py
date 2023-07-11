#!/usr/bin/python3
"""Module that defines a Student class"""


class Student:
    """Class that defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student object

        Args:
            first_name (str): The first name of the student
            last_name (str): The last name of the student
            age (int): The age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of the Student object

        If attrs is a list of strings, only attributes with names in attrs are
        included in the dictionary. Otherwise, all attributes are included.

        Args:
            attrs (list): A list of attribute names to include in the dict

        Returns:
            dict: A dictionary representation of the Student object
        """
        if attrs is None:
            return self.__dict__
        else:
            return {k: v for k, v in self.__dict__.items() if k in attrs}
