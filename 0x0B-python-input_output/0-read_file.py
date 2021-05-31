#!/usr/bin/python3
def read_file(filename=""):
    with open(filename) as f:
        lines = f.read()
        print(lines)
    f.closed
