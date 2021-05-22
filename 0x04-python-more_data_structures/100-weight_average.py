#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None:
        return(0)
    else:
        for g in range(len(my_list)):
            my_list[g] = my_list[g]
        return(my_list)
