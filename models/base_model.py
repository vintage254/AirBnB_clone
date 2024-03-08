#!/usr/bin/python3
"""Defines the Basemodel class"""
import uuid
import datetime
from models import storage

class BaseModel:
    """BaseModel class defining common attributes/methods."""

    def __init__(self):
        """Initialize BaseModel instance."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """Return string representation of BaseModel instance."""
        return "[{}] ({}) {}".format((
                self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """Update updated_at attribute with current datetime."""
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """Return dictionary rep of BaseModel instance."""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return (obj_dict)
