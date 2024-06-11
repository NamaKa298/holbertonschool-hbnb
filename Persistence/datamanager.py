import json
from typing import TypeVar, List, Dict
from Persistence.interface_persistence import IPersistenceManager


class DataManager(IPersistenceManager):

    def __init__(self):
        self.storage = {}  # For the sake of simplicity, we'll use a dictionary as our storage
        data = self.read_database()
        print("dsfsdfgsgdfgsdf", data)


    def read_database(self):
        try:
            with open('Persistence/database.json', 'r') as file:
                return json.load(file)
        except Exception:
            return {}

    def all(self, entity_type = None):
        if entity_type is None:
            return self.storage
        return self.storage.get(entity_type, {})

    def save(self, entity):
        entity_type = type(entity).__name__
        if entity_type not in self.storage:
            self.storage[entity_type] = {}
        self.storage[entity_type][entity.id] = entity
        with open('Persistence/database.json', 'w') as file:
            data = {}
            for entity_type in self.storage:
                data[entity_type] = {}
                for entity_id in self.storage[entity_type]:
                    data[entity_type][entity_id] = self.storage[entity_type][entity_id].to_dict()
            json.dump(data, file)

    def get(self, entity_id, entity_type):
        return self.storage.get(entity_type, {}).get(entity_id, None)

    def update(self, entity):
        entity_type = type(entity).__name__
        if entity_type in self.storage and entity.id in self.storage[entity_type]:
            self.storage[entity_type][entity.id] = entity

    def delete(self, entity_id, entity_type):
        if entity_type in self.storage and entity_id in self.storage[entity_type]:
            del self.storage[entity_type][entity_id]


data_manager = DataManager()
