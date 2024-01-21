#!/usr/bin/python3
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, String

"""
Module for the State class.
"""


class City(BaseModel, Base):
    """
        Represent a state.
        Attributes:
        name (str): The name of the state.
        """
    __tablename__ = "cities"
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    name = Column(String(128), nullable=False)
