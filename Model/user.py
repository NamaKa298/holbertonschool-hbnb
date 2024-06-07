from Model.BaseModel import BaseModel

users = {} # Need to be replaced by a database

class User(BaseModel):
    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)
        self.places = []
        users[self.email] = self

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
