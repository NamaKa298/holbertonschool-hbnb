from Model.BaseModel import BaseModel
import re

users = {} # Need to be replaced by a database

class User(BaseModel):
    
    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)
        self.places = []

    def get_full_name(self):
        return f"{self.firstname} {self.lastname}"

    @staticmethod
    def create(*args, **kargs):
        email = kargs.get("email")
        first_name = kargs.get("first_name")
        last_name = kargs.get("last_name")

        if not email or not User.is_valid_email(email):
                raise ValueError("Invalid email")
        if User.find_by_email(email):
                raise ValueError("Email already exists")
        if not first_name or not isinstance(first_name, str):
                raise ValueError("Invalid first name")
        if not last_name or not isinstance(last_name, str):
                raise ValueError("Invalid last name")

        return User(*args, **kargs)


    @staticmethod
    def find_by_email(email):
        return users.get(email)
        
    @staticmethod
    def is_valid_email(email):
        """Check if email is valid"""
        if re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return True
        return False