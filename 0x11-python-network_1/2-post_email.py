#!/usr/bin/python3
""" Post an email"""
import sys
import urllib.parse
import urllib.request

if __name__ == "__main__":
    data = {}
    data['email'] = sys.argv[2]
    url = sys.argv[1]

    data = urllib.parse.urlencode(data)
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        the_page = response.read().decode('utf8')
        print(the_page)
