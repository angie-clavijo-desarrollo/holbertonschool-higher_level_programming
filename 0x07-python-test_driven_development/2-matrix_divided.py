#!/usr/bin/python3
def matrix_divided(matrix, div):
    if type(matrix) == int and type(matrix) == float:
        return(matrix)
    if type(matrix) == None:
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    if len(matrix[0]) == len(matrix[1]):
        return(matrix)
    if len(matrix[0]) != len(matrix[1]):
        raise TypeError('Each row of the matrix must have the same size')
    if type(div) == int and type(div) == float:
        return(matrix)
    if type(div) == None:
        raise TypeError('div must be a number')
    if type(div) == 0:
        raise ZeroDivisionError('division by zero')
