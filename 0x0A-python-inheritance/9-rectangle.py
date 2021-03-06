#!/usr/bin/python3
"""This function import file 7 base geometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Class Rectangle
    That verify the area of rectangle
    in base width and height
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)

if __name__ == "__main__":
    r = Rectangle(3, 5)

    print(r)
    print(r.area())
