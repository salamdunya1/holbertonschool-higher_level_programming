#!/usr/bin/python3
"""
This script connects to a MySQL database
"""

import sys
import MySQLdb as mysql

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name_searched = sys.argv[4]

    db = mysql.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    cursor = db.cursor()
    cursor.execute("""
    SELECT *
    FROM states
    WHERE BINARY name = %s AND name IS NOT NULL
    ORDER BY id ASC;""".format(state_name_searched), (state_name_searched, ))
    result = cursor.fetchall()

    for x in result:
        print(x)

    cursor.close()
    db.close()
