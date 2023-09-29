#!/usr/bin/python3
"""2-post_email.py"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    if len(sys.argv) > 2:
        url = sys.argv[1]
        email = sys.argv[2]
        data = urllib.parse.urlencode({'email': email})
        data = data.encode('ascii')
        with urllib.request.urlopen(url, data) as response:
            print(response.read().decode('utf-8'))
