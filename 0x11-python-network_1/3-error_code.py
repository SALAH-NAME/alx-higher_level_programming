#!/usr/bin/python3
"""3-error_code.py"""
import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[1]
        try:
            with urllib.request.urlopen(url) as response:
                print(response.read().decode('utf-8'))
        except urllib.error.HTTPError as error:
            print("Error code: {}".format(error.code))
