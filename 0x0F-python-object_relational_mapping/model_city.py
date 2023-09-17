#!/usr/bin/python3
"""Define the City class which inherits from Base"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base, State


class City(Base):
    """
    Represents a city for a MySQL database.
    Attributes:
        id (sqlalchemy.Integer): The unique identifier of the city.
        name (sqlalchemy.String): The name of the city.
        state_id (sqlalchemy.Integer): The identifier of the state.
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
