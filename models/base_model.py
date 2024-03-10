#!/usr/bin/python3
import uuid
from datetime import datetime


class BaseModel:
    """
    Base class for other classes.

    Attributes:
        id (str): Unique identifier for instances.
        created_at (datetime): Date and time of instance creation.
        updated_at (datetime): Date and time of instance last update.
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize instance attributes.

        If keyword arguments provided:
            - Set attributes based on key-value pairs.
        Otherwise:
            - Generate a unique ID.
            - Set creation and update times to current UTC time.
        """
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, t_format))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()

    def save(self):

        """
        update public instance attribute updated_at with current datetime
        """
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """
        Return dictionary representation of instance attributes.

        Returns:
            dict: Dictionary containing all instance attributes.
        """
        instance_dict = self.__dict__.copy()
        instance_dict["__class__"] = self.__class__.__name__
        instance_dict["created_at"] = self.created_at.isoformat()
        instance_dict["updated_at"] = self.updated_at.isoformat()
        return instance_dict

    def __str__(self):
        """
        Return string representation of the instance.

        Returns:
            str: Formatted string containing class name,
            instance ID, and attributes.
        """
        class_name = self.__class__.__name__
        return ("[{}] ({}) {}".format(class_name, self.id, self.__dict__))
