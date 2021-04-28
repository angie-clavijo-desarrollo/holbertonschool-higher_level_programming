#!/usr/bin/python3
if __name__ == "__main__":
    def argument(*args):
        return(len(args))
    a = 1
    n = argument(1, 2, 4, a)
    print(argument(n), "{}".format(argument))
