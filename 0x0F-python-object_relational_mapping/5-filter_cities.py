#!/usr/bin/python3
"""Script that takes in the name of a state as an arg and lists all cities"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    st = "SELECT cities.name FROM cities \
        JOIN states ON cities.state_id = states.id \
        WHERE states.name=%s ORDER BY cities.id ASC"
    c.execute(st, (sys.argv[4],))
    rows = c.fechall()
    print(", ".join(row[0] for row in rows))
    c.close()
    db.clos()
