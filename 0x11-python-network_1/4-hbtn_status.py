#!/usr/bin/python3
""" Status code"""
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
        htm = ''
        print("Body response:")
        print("\t- type: {}".format(type(htm)))
        print("\t- content: {}".format(html.decode()))
