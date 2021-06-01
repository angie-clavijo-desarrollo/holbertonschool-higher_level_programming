#!/usr/bin/python3
"""Function save_to_json_file
"""


def class_to_json(obj):
    """Class to json
    Convert to class to a dictionary
    """
    return(obj.__dict__)
