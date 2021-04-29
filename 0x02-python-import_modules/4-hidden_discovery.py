#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    entry = 0
    for i in range (95, 123):
        entry = ord(sys.argv[i])
    print("{}".format(sys.argv[i]))
