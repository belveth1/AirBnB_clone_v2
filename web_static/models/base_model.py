#!/usr/bin/python3
import uuid
from datetime import datetime
import models


"""
Module for the BaseModel class.
"""


class BaseModel:
    time_format = "%Y-%m-%dT%H:%M:%S.%f"

    def __init__(self, *args, **kwargs):
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, time_format))
                else:
                    setattr(self, key, value)
        models.storage.new(self)

    def save(self):
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        data_dic = self.__dict__.copy()
        data_dic["__class__"] = self.__class__.__name__
        data_dic["created_at"] = self.created_at.isoformat()
        data_dic["updated_at"] = self.updated_at.isoformat()
        return data_dic

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)
