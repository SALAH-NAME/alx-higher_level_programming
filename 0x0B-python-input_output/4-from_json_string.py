#!/usr/bin/python3
"""
This module contains a function.
"""
import json


def from_json_string(my_str):
    """
    This function takes a JSON string as input and returns an object.
    """
    return json.loads(my_str)
