#!/usr/bin/python3
"""This script changes the name of a State object from the database."""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    ses = Session()
    state = ses.query(State).filter(State.id == 2).first()
    if state is not None:
        state.name = "New Mexico"
        ses.commit()
