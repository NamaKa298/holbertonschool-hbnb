from BaseModel import BaseModel

class Countries(BaseModel):
    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)

    def get_full_country(self):
        return f"{self.name}"

maDataDelaDatabase={"name":"France"}

country = Countries(**maDataDelaDatabase)

print(country.get_full_country(), country.__dict__)
