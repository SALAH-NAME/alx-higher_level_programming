#!/usr/bin/python3
"""
    Script that lists all states from the db where name matches the arg
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    st = "SELECT * FROM states WHERE name = {} ORDER BY id ASC"
    c = execute(st.format(sys.argv[4]))
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
    db.close()
