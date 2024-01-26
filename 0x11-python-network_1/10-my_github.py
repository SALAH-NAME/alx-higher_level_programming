#!/usr/bin/python3
"""10-my_github.py"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 2:
        username = sys.argv[1]
        token = sys.argv[2]
        response = requests.get(
                'https://api.github.com/user', auth=(username, token))
        if response.status_code >= 400:
            print("None")
        else:
            print(response.json().get('id'))
