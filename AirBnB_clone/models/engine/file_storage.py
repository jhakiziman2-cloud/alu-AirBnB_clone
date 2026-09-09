#!/usr/bin/python3
"""This module defines the FileStorage class, which serializes
instances to a JSON file and deserializes a JSON file back into
instances.
"""
import json


class FileStorage:
    """Serializes instances to a JSON file and deserializes a JSON
    file back to instances.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects, containing all currently
        stored objects keyed by '<class name>.<id>'.
        """
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key '<obj class name>.id'.

        Args:
            obj: The object instance to store.
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        serialized = {key: obj.to_dict()
                      for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(serialized, f)

    def reload(self):
        """Deserializes the JSON file to __objects, if it exists.

        If the JSON file (__file_path) does not exist, no exception
        is raised and nothing happens.
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review,
        }

        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            for key, value in data.items():
                cls_name = value["__class__"]
                FileStorage.__objects[key] = classes[cls_name](**value)
        except FileNotFoundError:
            pass
