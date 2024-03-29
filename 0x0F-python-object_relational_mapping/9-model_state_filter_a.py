#!/usr/bin/python3
"""Script lists all State objects that contain the letter 'a' from the db."""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    ses = Session()
    states = ses.query(State).filter(
            State.name.contains('a')).order_by(State.id)
    for state in states:
        print("{}: {}".format(state.id, state.name))
