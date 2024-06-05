from BaseModel import BaseModel

class Amenities(BaseModel):
    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)

    def get_full_amenity(self):
        return f"{self.name}"

maDataDelaDatabase={"name":"Microwave oven"}

amenity = Amenities(**maDataDelaDatabase)

print(amenity.get_full_amenity(), amenity.__dict__)
