#!/usr/bin/python3
"""Function append_write
"""


def append_write(filename="", text=""):
    """
    Function that append the file
    And mode write, encoding utf-8
    Print append of file extern
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        output = f.write(str(text))
        return output
