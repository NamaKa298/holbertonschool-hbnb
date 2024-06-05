from Model.user import User

class Reviewer(User):
    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)
