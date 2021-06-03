#!/usr/bin/python3
"""function print list in order"""


class MyList(list):
    """
    function that print in order
    parameter that is list
    """

    def print_sorted(self):
        print(sorted(self))


my_list = MyList()
my_list.append(1)
my_list.append(4)
my_list.append(2)
my_list.append(3)
my_list.append(5)
print(my_list)
my_list.print_sorted()
print(my_list)
