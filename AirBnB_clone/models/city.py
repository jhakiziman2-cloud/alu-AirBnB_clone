#!/usr/bin/python3
"""This module defines the City class, which represents a city
in the AirBnB clone application.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """Represents a city and inherits from BaseModel.

    Public class attributes:
        state_id (str): The id of the State the city belongs to.
        name (str): The name of the city.
    """

    state_id = ""
    name = ""
