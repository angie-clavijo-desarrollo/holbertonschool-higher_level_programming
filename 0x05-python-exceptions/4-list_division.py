#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    while list_length:
        try:
            result = my_list_1 / my_list_2
            print("Inside result: {}".format(result))
        except ZeroDivisionError:
            result = my_list_1 / my_list_2
            print("division by: {}".format(result))
        return result
