#!/usr/bin/python3
"""6-post_email.py"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 2:
        url = sys.argv[1]
        email = sys.argv[2]
        response = requests.post(url, data={'email': email})
        print(response.text)
