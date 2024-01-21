#!/usr/bin/python3
<<<<<<< HEAD
from models.base_model import BaseModel, Base
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
"""
Module for the State class.
"""
=======
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models import ValueEnv

>>>>>>> a0a0ad40d2c3a3754428c3863d95d0d37b8132c7

class State(BaseModel, Base):
    """ State class """
    if ValueEnv == "db":
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                              cascade='all, delete')
    else:
        name = ""

<<<<<<< HEAD
class State(BaseModel, Base):
    """
       Represent a state.

       Attributes:
           name (str): The name of the state.
       """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state',
                          cascade='all, delete-orphan')
=======
        @property
        def cities(self):
            """returns the list of Cities"""
            from models.city import City
            from models.__init__ import storage
            List_cities = []
            ALLcities = storage.all(City)
            for city in ALLcities.values():
                if city.state_id == self.id:
                    List_cities.append(city)
            return List_cities
>>>>>>> a0a0ad40d2c3a3754428c3863d95d0d37b8132c7
