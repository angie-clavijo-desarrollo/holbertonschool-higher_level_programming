#!/usr/bin/python3
"""Function save_to_json_file
"""
import json


def load_from_json_file(filename):
    """
    Function that write the file
    And mode write, encoding utf-8
    Save of datas of file extern
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)
