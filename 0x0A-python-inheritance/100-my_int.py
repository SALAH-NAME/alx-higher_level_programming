#!/usr/bin/python3
"""
This module defines the MyInt class
"""


class MyInt(int):
    """
    A class that inherits from int and has its == and != operators inverted
    """

    def __eq__(self, other):
        """
        Overrides the == operator to invert its behavior
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Overrides the != operator to invert its behavior
        """
        return super().__eq__(other)
