#!/usr/bin/python3
""" POST an email"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    data = {'email': sys.argv[2]}

    req = requests.post(url, data=data)
    print(req.text)
