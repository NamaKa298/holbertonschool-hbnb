from BaseModel import BaseModel

class User(BaseModel):
    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)

    def get_full_name(self):
        return f"{self.firstname} {self.lastname}"

maDataDelaDatabase={"firstname":"John","lastname":"Doe"}

user = User(**maDataDelaDatabase)

print(user.get_full_name(), user.__dict__)