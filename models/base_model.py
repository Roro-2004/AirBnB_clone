#!/usr/bin/python3

from datetime import datetime
import uuid
import models

"""
This is the Parent Class
"""


class BaseModel:
    """
    Defines all common attributes/methods
    for other classes
    """
    def __init__(self, *args, **kwargs):
        """
        intialize the class attributes
        """
        format = '%Y-%m-%dT%H:%M:%S.%f'
        if(len(kwargs) != 0):
            self.id = kwargs['id']
            self.created_at = datetime.strptime(kwargs['created_at'], format)
            self.updated_at = datetime.utcnow()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
        models.storage.new(self)

    def __str__(self):
        """
        returns a string representation of this object
        """
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """
        updates this object date
        """
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """
        returns a dict representation of this object
        """
        instance_dictionary = self.__dict__.copy()
        instance_dictionary['__class__'] = self.__class__.__name__
        instance_dictionary['created_at'] = self.created_at.isoformat()
        instance_dictionary['updated_at'] = self.updated_at.isoformat()
        return instance_dictionary
