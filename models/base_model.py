#!/usr/bin/python3
"""
    BaseModel that defines all common attributes/methods
    for other classes
"""


import uuid
from datetime import datetime, timezone


class BaseModel:
    """
    Defined BaseModel class and all public
    attributes and methods
    """

    def __init__(self):
        """
        initialization and assigning variables
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        should print: [<class name>] (<self.id>) <self.__dict__>
        """
        return "[{}] ({}) {}".format(
                self.__class__.__name__,
                self.id,
                self.__dict__
                )

    def save(self):
        """
        updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values
        of __dict__ of the instance, which is serialization
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__

        for key, value in obj_dict.items():
            """ converting datetime obj to ISO format """
            if isinstance(value, datetime):
                obj_dict[key] = value.isoformat()

        return obj_dict
