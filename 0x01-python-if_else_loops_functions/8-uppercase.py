#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        text = ord(str[i])
        if text in range(97, 123):
            text = text-32
        print("{}".format(chr(text)), end="")
    print()
