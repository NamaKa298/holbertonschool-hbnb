from Model.BaseModel import BaseModel
from Persistence.datamanager import DataManager

users = {} # Need to be replaced by a database

class User(BaseModel):
    data_manager = DataManager()
    
    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)
        self.places = []
        self.data_manager.save(self)

    def get_full_name(self):
        return f"{self.firstname} {self.lastname}"

    @staticmethod
    def create(*args, **kargs):
        if User.find_by_email(kargs.get("email")):
            raise ValueError("Email already exists")
        return User(*args, **kargs)

    @staticmethod
    def find_by_email(email):
        return users.get(email)
