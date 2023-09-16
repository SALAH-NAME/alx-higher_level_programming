#!/usr/bin/python3
"""Script that takes in the name of a state as an arg and lists all cities"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM cities c \
            JOIN states s ON s.id=c.state_id \
            ORDER BY c.id")
    rows = c.fetchall()
    print(", ".join([row[2] for row in rows if row[4] == sys.artv[4]]))
    c.close()
    db.close()
