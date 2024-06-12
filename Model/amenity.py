from Model.BaseModel import BaseModel

class Amenity(BaseModel):
    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)
        
    def get_full_amenity(self):
        return f"{self.name}"
