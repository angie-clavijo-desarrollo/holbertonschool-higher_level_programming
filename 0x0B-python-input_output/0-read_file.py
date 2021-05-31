#!/usr/bin/python3
def read_file(filename=""):
    with open(filename) as f:
        for line in f:
            read_data = f.read()
            print(line, end='')
    f.closed
