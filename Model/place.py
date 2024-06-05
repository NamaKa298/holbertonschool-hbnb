from BaseModel import BaseModel

class Places(BaseModel):
    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)

    def get_full_place(self):
        return f"{self.name} {self.description}"

maDataDelaDatabase={"name":"Villa sur les Hauteurs de la ville", "description":"Très belle maison en bord de mer"}

place = Places(**maDataDelaDatabase)

print(place.get_full_place(), place.__dict__)
