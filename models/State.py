#!/usr/bin/python3
from air_bnb.models.base_class import BaseModel, Base
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

"""
Module for the State class.
"""


class State(BaseModel, Base):
    """
       Represent a state.

       Attributes:
           name (str): The name of the state.
       """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade='all, delete-orphan')
