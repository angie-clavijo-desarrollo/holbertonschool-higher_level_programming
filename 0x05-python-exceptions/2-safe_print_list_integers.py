#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            i += 1
        print()
        return x
    except ValueError:
        if value != 0:
            return()
    except TypeError:
        if value != 0:
            return()
