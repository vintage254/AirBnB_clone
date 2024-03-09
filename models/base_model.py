#!/usr/bin/python3
import uuid
from datetime import datetime
"""
class BaseModel that defines all common attributes/methods for other classes
"""
class BaseModel:
    def __init__(self, *args, **kwargs):
        """
        if kwargs is not empty - each key of this dictionary is an attribute name (Note __class__ from kwargs is the only one that should not be added as an attribute.
        id: string - assign with an uuid when an instance is created
        created_at: datetime - assign with the current datetime when an instance is created
        updated_at: datetime - assign with the current datetime when an instance is created and it will be updated every time you change your object
        """
        t_format =  "%Y-%m-&dT&H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.item():
                if key == "__class__":
                    continue
                elif key == "created_at" or  "updated_at":
                    setattr(self, key, datetime.strptime(value, t_format))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
    def save(self):

        """
        updates the public instance attribute updated_at with the current datetime
        """
        self.updated_at = datetime.utcnow()
    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__ of the instance
        """
        instance_dict = self.__dict__.copy()
        instance_dict["__class__"] = self.__class__.__name__
        instance_dict["created_at"] = self.created_at.isoformat()
        instance_dict["updated_at"] = self.updated_at.isoformat()

        return instance_dict
    def __str__(self):
        class_name = self.__class__.__name__
        return ( "[{}] ({}) {}".format(class_name, self.id, self.__dict__))
