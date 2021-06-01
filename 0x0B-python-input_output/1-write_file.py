#!/usr/bin/python3
"""Function write_file
"""


def write_file(filename="", text=""):
    """
    Function that write the file
    And mode write, encoding utf-8
    Print len of datas of file extern
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        output = f.write(str(text))
        return output
