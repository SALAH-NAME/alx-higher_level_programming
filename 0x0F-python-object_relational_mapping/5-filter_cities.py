#!/usr/bin/python3
"""Script that takes in the name of a state as an arg and lists all cities"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT c.name FROM cities c \
        JOIN states c ON s.id=c.state_id \
        WHERE s.name=%s ORDER BY c.id", (sys.argv[4],))
    rows = c.fechall()
    print(", ".join(row[2] for row in rows))
    c.close()
    db.clos()
