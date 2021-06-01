#!/usr/bin/python3
"""Function save_to_json_file
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Function that write the file
    And mode write, encoding utf-8
    Save of datas of file extern
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
