#!/usr/bin/python3
"""created class that inherits of Base"""
from base import Base


class Rectangle(Base):

    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructor, instance attributes"""
        """call super class, with id, call with __init__ ,  or class parent"""
        super().__init__(id)
        """asignation"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    """getter and setter for each instance attributes"""
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        """validations"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    """update class Rectangle, add public method, return area value"""
    def area(self):
        return self.width * self.height

    """
    update class Rectangle, add public method,
    print # for width and height
    """
    def display(self):
        if self.width == 0 or self.height == 0:
            return ('')
        tmp = ('')
        for iter_one in range(self.__height):
            print("".join(["#" for i in range(self.__width)]))
        return (tmp)
        """pending exercise 7"""

    """Overriding method"""
    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.__x, self.__y, self.__width, self.__height)

    """method that assings argument to each attribute"""
    def update(self, *args):
        return "[Rectangle] ({}) {}/{} - {}/{}" \
            .format(self.id, self.width, self.height, self.x, self.y)


if __name__ == "__main__":
    r1 = Rectangle(10, 10, 10, 10)
    print(r1)

    r1.update(89)
    print(r1)

    r1.update(89, 2)
    print(r1)

    r1.update(89, 2, 3)
    print(r1)

    r1.update(89, 2, 3, 4)
    print(r1)

    r1.update(89, 2, 3, 4, 5)
    print(r1)
