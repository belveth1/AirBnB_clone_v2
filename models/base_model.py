#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
from models import ValueEnv

if ValueEnv == "db":
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """A base class for all hbnb models"""
    if ValueEnv == "db":
        id = Column(String(60), unique=True, nullable=False, primary_key=True)
        created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
        updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Initialize a new Base object.
        Args:
            args (won't be used): list of argumments.
            kwargs: pass in dictionary as argumment.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for attr, v in kwargs.items():
                # fix error: type of created_at and updated_at most be datetime
                if attr in ('created_at', 'updated_at'):
                    Nv = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, attr, Nv)
                elif attr != "__class__":
                    setattr(self, attr, v)

            # change move storage.new(self) to save()
            # models.storage.new(self)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models.__init__ import storage
        self.updated_at = datetime.now()
        # add storage.new(self) before storage.save()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        # delete key _sa_instance_state
        if '_sa_instance_state' in dictionary:
            del (dictionary['_sa_instance_state'])
        return dictionary

    # add method delete
    def to_delete(self):
        """method to delete an instance"""
        from models.__init__ import storage
        storage.delete(self)
