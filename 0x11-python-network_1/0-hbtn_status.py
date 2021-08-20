#!/usr/bin/python3
# script that fetches url
import urllib.request


with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    html = response.read()
    types = type(html)
    print("Body response:\n\t",
          "- type: {}\n\t".format(types),
          "- content: {}\n\t".format(html),
          "- utf8 content: {}".format(html.decode()))
