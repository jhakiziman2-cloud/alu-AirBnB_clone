#!/usr/bin/python3
"""This module defines the BaseModel class, the parent class for all
other models in the AirBnB clone project. It takes care of the
initialization, serialization and deserialization of future instances.
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """Defines common attributes/methods for other classes in the
    project.
    """

    def __init__(self, *args, **kwargs):
        """Initializes a new BaseModel instance.

        Args:
            *args: Unused positional arguments.
            **kwargs: Key/value pairs used to re-create an instance
                from a dictionary representation. If provided, each
                key becomes an instance attribute (except
                '__class__'). 'created_at' and 'updated_at' are
                converted from ISO format strings into datetime
                objects.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in ("created_at", "updated_at"):
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
            if "created_at" not in kwargs:
                self.created_at = datetime.now()
            if "updated_at" not in kwargs:
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Returns the string representation of the BaseModel
        instance in the format: [<class name>] (<id>) <__dict__>.
        """
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Updates 'updated_at' with the current datetime and saves
        the instance to the JSON file via the storage engine.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary representation of the instance.

        The returned dictionary contains all keys/values of
        __dict__, with '__class__' added as the class name of the
        object, and 'created_at'/'updated_at' converted to ISO
        format strings.
        """
        dict_copy = self.__dict__.copy()
        dict_copy["__class__"] = type(self).__name__
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()
        return dict_copy
