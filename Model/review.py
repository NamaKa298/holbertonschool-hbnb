from Model.BaseModel import BaseModel

class Review(BaseModel):
    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)

    def get_full_review(self):
        return f"{self.text}"


