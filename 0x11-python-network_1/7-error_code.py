#!/usr/bin/python3
""" Error code"""
from requests.exceptions import HTTPError, Timeout
import requests
import sys

if __name__ == "__main__":
    try:
        url = sys.argv[1]
        req = requests.get(url)
        print(req)
    except HTTPError as error:
        print(f'Http Error: {error}')
