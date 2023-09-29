#!/usr/bin/python3
"""7-error_code.py"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[1]
        try:
            response = requests.get(url)
            response.raise_for_status()
            print(response.text)
        except requests.exceptions.HTTPError as errh:
            print("Error code: {}".format(errh.response.status_code))
