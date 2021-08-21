#!/usr/bin/python3
""" Search API"""
import requests
import sys

if __name__ == "__main__":
    url = ('http://880d559bbb2f.4fd667c2.hbtn-cod.io:5000/search_user')

    if (len(sys.argv) > 1):
        data = {'q': sys.argv[1]}
    else:
        data = {'q': ""}

    req = requests.post(url, data)
    
    try:
        if len(r.json()) == 0:
            print("No result")
        else:
            print("[{}] {}".format(r.json().get('id'), r.json.get('name')))
    except:
        print("Not a valid JSON")
