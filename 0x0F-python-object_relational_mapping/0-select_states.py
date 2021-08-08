#!/usr/bin/python3
"""
Module for conneting to MYSQLdb datbase
and view the arguments of the database
and verify dabase created and finally print agrv's
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
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
    result = cursor.fetchall()
    for row in result:
        print(row)

    # disconect from server
    cursor.close()
    db.close()