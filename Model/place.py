from Model.BaseModel import BaseModel
from Model.user import User


class Place(BaseModel):
    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)
        self.amenities = []


    def get_full_place(self):
        return f"{self.name} {self.description}"


    @classmethod
    def create(cls, host, *args, **kargs):
        if not isinstance(host, User):
            raise ValueError("Host must be a User instance")
        place = cls(host=host, *args, **kargs)
        host.places.append(place)
        return place


