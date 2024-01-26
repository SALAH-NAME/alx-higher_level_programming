#!/usr/bin/python3
"""1-hbtn_header.py"""
import urllib.request
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[1]
        with urllib.request.urlopen(url) as response:
            print(response.getheader('X-Request-Id'))
