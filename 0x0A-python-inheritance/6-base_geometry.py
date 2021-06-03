#!/usr/bin/python3
"""function that created a class"""


class BaseGeometry:
    """
    function that created a class
    validate if area is implement
    """
    def area(self):
        raise Exception('area() is not implemented')

if __name__ == "__main__":
    bg = BaseGeometry()

    try:
        print(bg.area())
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
