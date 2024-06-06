from BaseModel import BaseModel

class User(BaseModel):
    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)
        self.places = []

    def get_full_name(self):
        return f"{self.firstname} {self.lastname}"

    @classmethod
    def create(cls, email, *args, **kargs):
        if cls.find_by_email(email):
            raise ValueError("Email already exists")
        return cls(email=email, *args, **kargs)

    @classmethod
    def find_by_email(cls, email):
        pass


maDataDelaDatabase={"firstname":"John","lastname":"Doe"}

user = User(**maDataDelaDatabase)

print(user.get_full_name(), user.__dict__)