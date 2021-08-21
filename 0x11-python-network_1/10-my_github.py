#!/usr/bin/python3
""" GitHub API"""
import requests
import sys

if __name__ == "__main__":
    url = 'https://api.github.com/user'

    req = requests.get(url, auth=(sys.argv[1], sys.argv[2]))

    json = req.json()
    try:
        print(json['id'])
    except:
        print("None")
