#!/usr/bin/python3
# script that fetches url
import urllib.request
with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    html = response.read()
    print('-', html)
