#!/usr/bin/python3
""" response header and request """
import urllib.request
import sys

if __name__ == "__main__":
    req =  urllib.request.urlopen(sys.argv[1])
    print(req.getheader("X-Request-Id"))
