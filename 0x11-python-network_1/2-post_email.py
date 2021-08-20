#!/usr/bin/python3
""" Post an email"""
import sys
import urllib.parse
import urllib.request

if __name__ == "__main__":

    email = {'email': sys.argv[2]}
    url = sys.argv[1]

    data = urllib.parse.urlencode(email)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data, email)
    with urllib.request.urlopen(req) as response:
        the_page = response.read().decode('utf8')
        print(the_page)
