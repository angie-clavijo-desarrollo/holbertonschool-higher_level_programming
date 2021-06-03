#!/usr/bin/python3
"""function that verify if is to same class"""


def is_same_class(obj, a_class):
    """
    function verify if is to same class
    parameter that is class
    """
    if type(obj) == a_class:
        return True

if __name__ == "__main__":
    a = 1
    if is_same_class(a, int):
        print("{} is an instance of the class {}".format(a, int.__name__))
    if is_same_class(a, float):
        print("{} is an instance of the class {}".format(a, float.__name__))
    if is_same_class(a, object):
        print("{} is an instance of the class {}".format(a, object.__name__))
