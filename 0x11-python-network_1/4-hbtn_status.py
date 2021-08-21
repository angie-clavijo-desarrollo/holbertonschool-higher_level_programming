#!/usr/bin/python3
""" Status code"""
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(text)))
        print("\t- content: {}".format(type(text)))
