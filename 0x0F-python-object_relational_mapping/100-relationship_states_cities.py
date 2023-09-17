#!/usr/bin/python3
"""Script that creates the State “C” with the City “S F” from the db"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    cal = State(name='California')
    sf = City(name='San Francisco', state=cal)
    session.add(sf)
    session.add(cal)
    session.commit()
