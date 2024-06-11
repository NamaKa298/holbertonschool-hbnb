from Model.BaseModel import BaseModel

class City(BaseModel):
    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)

    def get_full_city(self):
        return f"{self.name}"


