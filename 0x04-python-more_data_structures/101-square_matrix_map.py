#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda count1: list(map
                    (lambda count2: count2**2, count1)), matrix))
