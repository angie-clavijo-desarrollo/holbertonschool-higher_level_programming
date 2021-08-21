#!/usr/bin/python3
""" POST an email"""
import requests
import sys

if __name__ == "__main__":
    req = requests.post(sys.argv[1])
    print('Your email is: {}'.format(sys.argv[2]))
