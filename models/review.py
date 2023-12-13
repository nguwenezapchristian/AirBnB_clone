#!/usr/bin/python3
"""
Review class Module
"""
from .base_model import BaseModel

class Review(BaseModel):
    """
    Represents a review

    Attributes:
        place_id(str): The place id.
        user_id (str): The user id.
        text (str): The text of the review.
     """

    place_id = ""
    user_id = ""
    text = ""
