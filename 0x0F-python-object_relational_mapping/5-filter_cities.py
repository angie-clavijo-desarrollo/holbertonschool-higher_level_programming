#!/usr/bin/python3
"""
Module for connecting to MYSQLdb database
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
    cursor.execute(" SELECT cities.name FROM cities\
                    INNER JOIN states ON cities.state_id = states.id\
                    WHERE states.name = %s;", [argv[4]])
    result = cursor.fetchall()
    output = []
    for row in result:
        output.append(row[0])
    print(*output, sep=", ")

    # disconnect from server
    cursor.close()
    db.close()
