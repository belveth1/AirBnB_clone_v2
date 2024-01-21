#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship
from models import ValueEnv


<<<<<<< HEAD

class City(BaseModel, Base):
    """
        Represent a state.
        Attributes:
        name (str): The name of the state.
        """
    __tablename__ = "cities"
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    name = Column(String(128), nullable=False)
=======
class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    if ValueEnv == "db":
        __tablename__ = 'cities'
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
        places = relationship("Place", backref="cities", cascade="all,delete")
    else:
        name = ""
        state_id = ""
>>>>>>> a0a0ad40d2c3a3754428c3863d95d0d37b8132c7
