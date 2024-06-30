#!/usr/bin/python3
"""lists all states"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db_connection = MySQLdb.connect(
        host='localhost', port=3306, user=argv[1], passwd=argv[2], db=argv[3])

    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id")
    rows = cursor.fetchall()

    for row in rows:
        print(row)
    cursor.close()
    db_connection.close()
