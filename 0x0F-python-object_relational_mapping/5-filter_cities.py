#!/usr/bin/python3
"""Script that takes in the name of a state as an arg and lists all cities"""


import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT cities.name FROM cities \
                JOIN states ON cities.state_id = states.id \
                WHERE states.name=%s ORDER BY cities.id ASC", (sys.argv[4],))
    rows = c.fetchall()
    print(", ".join(row[0] for row in rows))
    c.close()
    db.close()
