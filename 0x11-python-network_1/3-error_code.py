#!/usr/bin/python3
""" Error code"""
import urllib.request
from urllib.error import URLError, HTTPError
import sys

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            html = response.read().decode('utf8')
            print(html)
    except urllib.error.HTTPError as error:
        print("Error code: {}".format(error.code))
