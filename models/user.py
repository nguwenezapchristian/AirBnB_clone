#!/usr/bin/python3
"""
Module for the UserClass
"""

from models.base_model import BaseModel

class User(BaseModel):
    """
    User class information handler
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
