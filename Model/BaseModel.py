#!/usr/bin/python3
"""This module defines the BaseModel class"""


from datetime import datetime
import uuid


class BaseModel:
    """Represent the base class for all models in the application"""

    def __init__(self, *args, **kwargs) -> None:
        """
            Initialize a new instance of the BaseModel class
            Please don't instantiate this class directly,
            instead use it as a base class for other classes
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if (kwargs):
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
                    print(f"{key} = {value}")
        
        if (args):
            for key, value in args.items():
                setattr(self, key, value)
                print(f"{key} = {value}")

    def save(self):
        self.updated_at = datetime.now()
        # Logique de base de données