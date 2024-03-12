#!/usr/bin/python3
from models.base_model import BaseModel
import json
import os
""" file storage class"""


class FileStorage:
    """a class that handels the storage of data in json
    Attributes:
            file_path: a private variable that contains
            the path of created file
            objects: a private dictionary that will carry
             the items from the file"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """getter for the dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """setter for the object"""
        key = obj.__class__.__name__ + '.' + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """serializing data into the file"""
        all_data = FileStorage.__objects
        saved = {}
        for k in all_data.keys():
            saved[k] = all_data[k].to_dict()
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(saved, file)

    def reload(self):
        """deserializing data from file"""
        if(os.path.isfile(FileStorage.__file_path)):
            with open(FileStorage.__file_path, 'r') as json_file:
                try:
                    from_file_data = json.load(json_file)
                    for k, val in from_file_data.items():
                        class_name, obj_id = k.split('.')

                        new_inst = eval(class_name)
                        to_be_added = new_inst(**val)
                        FileStorage.__objects[k] = to_be_added
                except Exception:
                    pass
