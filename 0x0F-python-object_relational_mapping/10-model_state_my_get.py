#!/usr/bin/python3
"""Script prints the State object with the name passed as an arg from the db"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    ses = Session()
    state = ses.query(State).filter(State.name == sys.argv[4]).first()
    if state is not None:
        print(state.id)
    else:
        print("Not found")
