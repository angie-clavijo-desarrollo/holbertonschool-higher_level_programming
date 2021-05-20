#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        int(value)
        print("{:d}".format(value))
        return(True)
        raise
    except ValueError as ex:
        print("Exception:{}".format(ex), file=sys.stderr)
        return(False)
    except:
        print("Exception:{}".format(), file=sys.stderr)
        return(False)
