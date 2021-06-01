#!/usr/bin/python3
"""Function read_file
"""


def read_file(filename=""):
    """
    Function that read other file
    As with that open file
    And mode read, encoding utf-8
    Print lines of file extern
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        lines = f.read()
        print(lines, end="")
