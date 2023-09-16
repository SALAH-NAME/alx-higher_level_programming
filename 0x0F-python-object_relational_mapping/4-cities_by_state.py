#!/usr/bin/python3
"""A script that lists all cities from the database hbtn_0e_4_usa."""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT c.id, c.name, s.name FROM cities as c \
                JOIN states as s ON s.id = c.state_id \
                ORDER BY c.id ASC")
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
    db.close()
