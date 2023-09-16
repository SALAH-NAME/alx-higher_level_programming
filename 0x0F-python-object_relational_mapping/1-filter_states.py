#!/usr/bin/python3
"""Script that lists all states with a name starting with N from the db"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `states` ORDER BY `id`")
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
    db.close()
