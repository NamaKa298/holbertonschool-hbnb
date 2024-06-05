from Model.BaseModel import BaseModel

class Reviews(BaseModel):
    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)

    def get_full_review(self):
        return f"{self.text}"

maDataDelaDatabase={"text":"Cette Maison ne correspond pas du tout aux photos"}

review = Reviews(**maDataDelaDatabase)

print(review.get_full_review(), review.__dict__)
