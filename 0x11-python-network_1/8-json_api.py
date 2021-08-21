#!/usr/bin/python3
""" Search API"""
import requests
import sys

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    data = {}

    if len(sys.argv) > 1:
        data = {'q': sys.argv[1]}
    else:
        data = {'q': ""}

    req = requests.post(url, data=data)
    try:
        size = req.json()
        if size == {}:
            print("No result")
        else:
            print("[{}] {}".format(size["id"], size["name"]))
    except ValueError:
        print("Not a valid JSON")
