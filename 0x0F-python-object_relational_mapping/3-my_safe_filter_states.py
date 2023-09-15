#!/usr/bin/python3
"""
display all values in the state table of DTbase hbtn_0e_0_usa
whose name matches that supplied as argument
Safe from SQL injections.
usage -> ./3-may_safe_filter_states.py <mysql username>\
              <mysql password>\
              <database name>\
              <state name searched>

"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `states`")
    [print(state) for state in c.fetchall() if state[1] == sys.argv[4]]
