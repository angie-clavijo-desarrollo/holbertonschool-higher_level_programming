#!/usr/bin/python3
"""
Module for connecting to MySQLdb database
and view the arguments of the database
and doing query at database
"""
import MySQLdb
from sys import argv


# expression not execute when load
if __name__ == "__main__":

    # to connect
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    # prepare cursor object cursor () method
    cursor = db.cursor()

    # Execute sql query  using execute method
    var_of_query = "SELECT * FROM states WHERE name \
                    LIKE BINARY '{}'".format(argv[4])
    # Var and execute
    cursor.execute(var_of_query)
    result = cursor.fetchall()
    for row in result:
        print(row)

    # disconnect from server
    cursor.close()
    db.close()
