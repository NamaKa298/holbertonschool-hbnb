from Model.BaseModel import BaseModel

class Cities(BaseModel):
    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)

    def get_full_city(self):
        return f"{self.name}"

maDataDelaDatabase={"name":"Saint Tropez"}

city = Cities(**maDataDelaDatabase)

print(city.get_full_city(), city.__dict__)
