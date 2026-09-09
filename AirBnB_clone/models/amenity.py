#!/usr/bin/python3
"""This module defines the Amenity class, which represents an
amenity that can be attached to a place in the AirBnB clone
application.
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represents an amenity and inherits from BaseModel.

    Public class attributes:
        name (str): The name of the amenity.
    """

    name = ""
