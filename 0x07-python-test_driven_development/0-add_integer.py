#!/usr/bin/python3
"""
This module contains a function that adds two integers or floats.
"""
def add_integer(a, b=98):
    """
    This function adds two numbers and returns the result as an integer.
    If either argument is not an integer or float, a TypeError is raised.
    The function will also fail if infinity or NaN numbers are provided as arguments.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
