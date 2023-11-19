#!/usr/bin/python3

"""
Script that listes all states with a name starting
with N  from DB
"""

import sys
import MySQLdb

if __name__ == "__main__":
    """
    check if the script is being run with the correct number
    of arguments
    """
    if len(sys.argv) != 4:
        print("Usage: {} <mysql_username> <mysql_password> \
                <database_name>".format(sys.argv[0]))
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    """
    connect to MYSQL-SERVER
    """
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=database_name
            )

    """
    cursor object to excute queries
    """
    cursor = db.cursor()

    """
    excute the query to select states starting with 'N'
    """
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY ID ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    """
    close the cursor andn db connection
    """
    cursor.close()
    db.close()
