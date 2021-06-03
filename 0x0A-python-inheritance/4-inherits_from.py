#!/usr/bin/python3
"""function that verify from is inherited"""


def inherits_from(obj, a_class):
    """
    function that verify from is inherited
    parameter that is class
    """
    if type(obj) != a_class and (isinstance(obj, a_class)):
        return True


if __name__ == "__main__":
    a = True
    if inherits_from(a, int):
        print("{} inherited from class {}".format(a, int.__name__))
    if inherits_from(a, bool):
        print("{} inherited from class {}".format(a, bool.__name__))
    if inherits_from(a, object):
        print("{} inherited from class {}".format(a, object.__name__))
