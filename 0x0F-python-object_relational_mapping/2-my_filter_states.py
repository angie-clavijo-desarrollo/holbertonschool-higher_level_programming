#!/usr/bin/python3
import sys
import MySQLdb
from sys import argv
"""Module for conneting to MYSQL datbase"""

"""expression not execute when load"""
if __name__ == "__main__":

    """to connect"""
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    """prepare cursor object cursor () method"""
    cursor = db.cursor()

    """Execute sql query  using execute method"""
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
#    cursor.execute("SELECT * FROM states WHERE  states.id LIKE '2%'")#
    cursor.execute("SELECT * FROM states WHERE name='Arizona'")
    result = cursor.fetchall()
    for row in result:
        print(row)

    """disconect from server"""
    cursor.close()
    db.close()
