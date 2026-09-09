#!/usr/bin/python3
"""This module defines the State class, which represents a state
in the AirBnB clone application.
"""
from models.base_model import BaseModel


class State(BaseModel):
    """Represents a state and inherits from BaseModel.

    Public class attributes:
        name (str): The name of the state.
    """

    name = ""
