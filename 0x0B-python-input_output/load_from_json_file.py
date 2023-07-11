#!/usr/bin/python3
"""
This module contains a function.
"""
import json


def load_from_json_file(filename):
    """
    This function creates an object from a JSON file.
    """
    with open(filename, 'r') as f:
        return json.load(f)
