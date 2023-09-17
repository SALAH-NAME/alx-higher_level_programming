#!/usr/bin/python3
"""This script defines a State class and creates a MySQL table states."""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    State class that inherits from Base.
    This class is linked to the MySQL table states.
    Attributes:
        id: Represents a column of an auto-generated, unique integer,
        name: Represents a column of a string with maximum 128 characters
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
