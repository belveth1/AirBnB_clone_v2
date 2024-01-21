#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models import ValueEnv


class State(BaseModel, Base):
    """ State class """
    if ValueEnv == "db":
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                              cascade='all, delete')
    else:
        name = ""

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
