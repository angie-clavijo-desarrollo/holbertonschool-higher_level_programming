#!/usr/bin/python3
"""import functions of file calculator, * all"""
    if __name__ == "__main__":
    from calculator_1 import *
    a = 10
    b = 5
    print("{:d} + {:d} =" .format(a, b), add(a, b))
    print("{:d} - {:d} =" .format(a, b), sub(a, b))
    print("{:d} * {:d} =" .format(a, b), mul(a, b))
    print("{:d} / {:d} =" .format(a, b), div(a, b))
