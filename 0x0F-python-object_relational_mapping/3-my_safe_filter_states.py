#!/usr/bin/python3
"""
Script that lists all states from the db where name matches the arg
This version is safe from SQL injections.
"""

import MySQLdb
import sys

if __name__ = "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.arv[2], db=sys.argv[3])
    c = db.cursor()
    st = "SELECT * FROM states ORDER BY id ASC"
    c.execute(st)
    rows = c.fetchall()
    for row in rows:
        if row[1] == sys.argv[4]:
            print(row)
    c.close()
    db.close()
