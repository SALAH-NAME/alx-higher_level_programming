#!/usr/bin/python3
"""
This module contains the MyList.
"""


class MyList(list):
    """Implements sorted printing for the built-in list class."""
    def print_sorted(self):
        """
        This method prints the list in ascending order.
        """
        print(sorted(self))
