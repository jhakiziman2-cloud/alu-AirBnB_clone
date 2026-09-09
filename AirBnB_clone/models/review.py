#!/usr/bin/python3
"""This module defines the Review class, which represents a review
left on a place in the AirBnB clone application.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represents a review and inherits from BaseModel.

    Public class attributes:
        place_id (str): The id of the Place being reviewed.
        user_id (str): The id of the User who wrote the review.
        text (str): The content of the review.
    """

    place_id = ""
    user_id = ""
    text = ""
