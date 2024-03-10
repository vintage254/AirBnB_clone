#!/usr/bin/python3
""" File Storage Module Documentation """
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
    File Storage Class

    This class manages the serialization and deserialization of instances
    of the different models to and from JSON files.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Retrieve all objects.

        Return the dictionary __objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Add a new object to the dictionary.

        set in __objects obj to be added with key 
        """
        id = obj.to_dict()["id"]
        className = obj.to_dict()["__class__"]
        keyName = className+"."+id
        FileStorage.__objects[keyName] = obj

    def save(self):
        """ Save obj to JSON file """
        filepath = FileStorage.__file_path
        data = dict(FileStorage.__objects)
        for key, value in data.items():
            data[key] = value.to_dict()
        with open(filepath, 'w') as f:
            json.dump(data, f)

    def reload(self):
        """
         Reload objects from JSON file.
        """
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
