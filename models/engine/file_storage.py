#!/usr/bin/python3
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.city import City

"""
Module for serializing and deserializing data
"""


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Args:
                    cls (class, optional): If specified,
                    filters the result to include
                    only objects of the specified class.

                Returns:
                    dict: A dictionary containing objects in storage.
                """
        if cls:
            if isinstance(cls, str):
                cls = globals().get(cls)
            if cls and issubclass(cls, BaseModel):
                cls_dict = {k: v for k,
                            v in self.__objects.items() if isinstance(v, cls)}
                return cls_dict
        return FileStorage.__objects

    def new(self, obj):
        obj_cls_name = obj.__class__.__name__
        key = "{}.{}".format(obj_cls_name, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        all_objs = FileStorage.__objects
        obj_dict = {}
        for obj in all_objs.keys():
            obj_dict[obj] = all_objs[obj].to_dict()
            with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
                json.dump(obj_dict, file)

    def reload(self):
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                try:
                    obj_dict = json.load(file)

                    for key, value in obj_dict.items():
                        class_name, obj_id = key.split('.')

                        cls = eval(class_name)

                        instance = cls(**value)

                        FileStorage.__objects[key] = instance
                except Exception:
                    pass

    def delete(self, obj=None):
        """
            Delete obj from __objects if it’s inside - if obj is equal to None,
            the method should not do anything
                """
        if obj:
            obj_to_del = "{}.{}".format(obj.__class__.__name__, obj.id)
            try:
                del FileStorage.__objects[obj_to_del]
            except AttributeError:
                pass
            except KeyboardInterrupt:
                pass
