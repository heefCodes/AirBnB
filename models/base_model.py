#!/usr/bin/python3
"""
BaseModel class definition
"""
import uuid 
from datetime import datetime

class BaseModel():
    """
    BaseModel that defines all common attributes/methods
    for other classes.
    """
    def __init__(self, id, created_at, updated_at):
        """
        To initializes the public instance attributes
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        print the attributes in string format
        """
        return f"[{self.__class__.__name__}] ({self.id} {self.__dict__})"

    def save(self):
        """
        public instance method to updates the public instance
        attribute update_at with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        to return a dictionary containing all keys/values of the instance
        """
        self.created_at = now.strftime(%Y-%m-%dT%H:%M:%S.%f)
        self.updated_at = now.strftime(%Y-%m-%dT%H:%M:%S.%f)
        self.__dict__['__class__'] = self.__class__.__name__
        return self.__dict__