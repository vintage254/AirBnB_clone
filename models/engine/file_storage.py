#!/usr/bin/python3
""" File Storage Module for serialization and deserialization"""
from json import dump, load
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage


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
        obj_class_name = obj.__class__.__name__
        obj_id = obj.id

        FileStorage.__objects[obj_class_name + '.' + obj_id] = obj

    def save(self):
        """ Save obj to JSON file """
        allobj_dict = FileStorage.__objects

        formatted_objects_dict = \
            {key: allobj_dict[key].to_dict() for key in allobj_dict.keys()}

        with open(FileStorage.__file_path, "w", encoding='utf-8') as json_file:
            dump(formatted_objects_dict, json_file)

    def reload(self):
        """
         Reload objects from JSON file.
        """
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                json_object = load(f)

                for key, value in json_object.items():
                    cls_name, object_id = key.split('.')
                    cls = getattr(models, cls_name)
                    instance = cls(**value)
                    FileStorage.__objects[key] = instance
        except FileNotFoundError:
            pass
