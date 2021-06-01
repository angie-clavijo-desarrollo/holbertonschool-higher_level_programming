#!/usr/bin/python3
import json
"""Function def to_json_string
"""


def to_json_string(my_obj):
    """
    Function that return the file.json
    And mode write, encoding utf-8
    Print return string of file extern
    """
    with open('my_obj', mode="w", encoding="utf-8") as f:
        return json.dumps(my_obj)
