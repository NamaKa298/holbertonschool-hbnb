import json
from datetime import datetime
import uuid

data = {}

class BaseModel:
    """Represent the base class for all models in the application"""

    def __init__(self, *args, **kwargs) -> None:
        """
            Initialize a new instance of the BaseModel class
            Please don't instantiate this class directly,
            instead use it as a base class for other classes
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if (kwargs):
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
                    print(f"{key} = {value}")
        
        if (args):
            for key, value in args.items():
                setattr(self, key, value)
                print(f"{key} = {value}")
    
    @classmethod
    def exists(cls, entity):
        cls_entities = data.get(cls.__name__)
        return (
            True if cls_entities 
            and cls_entities.get(entity.id) 
            else False
        )

    @classmethod
    def create(cls, *args, **kwargs):
        try:
            if (data[cls.__name__]):
                instance = cls(*args, **kwargs)
                if (cls.exists(instance)):
                    return cls.create(*args, **kwargs)
                data[cls.__name__][kwargs["id"]] = instance
                return instance
            else:
                data[cls.__name__] = {}
                return cls.create(*args, **kwargs)
        except Exception as e:
            print(f"An error occured while creating instance of {cls.__name__}.\n{e}")


    def to_dict(self):
        """Return a dictionary representation of the instance for JSON"""
        return {
            'id': self.id,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
        }

    @classmethod
    def from_dict(cls, data):
        """Create an instance from a dictionary"""
        if 'created_at' in data:
            data['created_at'] = datetime.strptime(data['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
        if 'updated_at' in data:
            data['updated_at'] = datetime.strptime(data['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")
        return cls(**data)

    def save_to_file(self):
        """Save the instance to a JSON file"""
        self.updated_at = datetime.now()
        with open(f'{self.id}.json', 'w') as f:
            json.dump(self.to_dict(), f)

    @classmethod
    def load_from_file(cls, id):
        """Load an instance from a JSON file"""
        with open(f'{id}.json', 'r') as f:
            data = json.load(f)
        return cls.from_dict(data)