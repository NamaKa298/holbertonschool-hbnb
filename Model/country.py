from Model.BaseModel import BaseModel

class Country(BaseModel):
    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)

    def get_full_country(self):
        return f"{self.name}"


