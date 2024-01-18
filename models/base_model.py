#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import models
<<<<<<< HEAD
import uuid
import datetime

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime

=======
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String
>>>>>>> 961da3cd70a2d4517e5575d42d00829ba4de43aa

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""

    id = Column(String(60), primary_key=True,
                nullable=False, unique=True)
    created_at = Column(DateTime, nullable=False,
                        default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, nullable=False,
                        default=datetime.datetime.utcnow,
                        onupdate=datetime.datetime.utcnow)

    def __init__(self, *args, **kwargs) -> None:
        """Initialization of BaseModel Class"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    date = datetime.datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, date)
                elif key != "__class__":
                    setattr(self, key, value)
<<<<<<< HEAD

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.datetime.now()
=======

    def save(self):
        self.updated_at = datetime.utcnow()
>>>>>>> 961da3cd70a2d4517e5575d42d00829ba4de43aa
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
<<<<<<< HEAD
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if '_sa_instance_state' in dictionary:
            del dictionary['_sa_instance_state']
        return dictionary

    def delete(self):
        """Docs"""
=======
        data_dic = self.__dict__.copy()
        data_dic["__class__"] = self.__class__.__name__
        data_dic["created_at"] = self.created_at.isoformat()
        data_dic["updated_at"] = self.updated_at.isoformat()
        try:
            del data_dic["_sa_instance_state"]
        except KeyError:
            pass
        return data_dic

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def delete(self):
>>>>>>> 961da3cd70a2d4517e5575d42d00829ba4de43aa
        models.storage.delete(self)
