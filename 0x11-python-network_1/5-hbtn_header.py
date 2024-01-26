#!/usr/bin/python3
"""5-hbtn_header.py"""
import requests
import sys


if __name__ == '__main__':
    if len(sys.argv) > 1:
        url = sys.argv[1]
        response = requests.get(url)
        print(response.headers.get('X-Request-Id'))
