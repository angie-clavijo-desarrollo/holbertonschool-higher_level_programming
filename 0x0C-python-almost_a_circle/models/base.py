#!/usr/bin/python3
"""created class"""


class Base:

    """class attribute, private"""
    __nb_objects = 0

    """class constructor, instance attributes"""
    def __init__(self, id=None):
        if id is not None:
            """asign  instance attribute, public"""
            self.id = id
        else:
            """increment attribute of class"""
            Base.__nb_objects += 1
            """and assign the new value of __nb...
            to the instance atrribute, public id"""
            self.id = self.__nb_objects

if __name__ == "__main__":
    b1 = Base()
    print(b1.id)

    b2 = Base()
    print(b2.id)

    b3 = Base()
    print(b3.id)

    b4 = Base(12)
    print(b4.id)

    b5 = Base()
    print(b5.id)
