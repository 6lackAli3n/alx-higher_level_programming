#!/usr/bin/python3
import json


class Base:
    """Base class for managing id attribute"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor method for Base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        if list_objs is None:
            list_objs = []
            filename = cls.__name__ + ".json"
            with open(filename, "w") as file:
                json_string = cls.to_json_string(
                        [obj.to_dictionary() for obj in list_objs])
                file.write(json_string)
