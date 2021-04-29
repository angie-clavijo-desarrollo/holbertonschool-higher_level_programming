#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for i in dir(hidden_4):
        if(i[0] != '_'):
            print("{}".format(i))

    """file  "hidden_4.pyc", in <module>
    from Normalization import dir(hidden_4)
    </module>"""
    """import hidden_4
    if hidden_4 != str("__"):
        print("{}".format(hidden_4))"""
    """import sys
    entry = 0
    for i in range (95, 123):
        entry = ord(sys.argv[i])
    print("{}".format(sys.argv[i]))"""
