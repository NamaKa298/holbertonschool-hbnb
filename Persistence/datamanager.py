from typing import TypeVar, List, Dict
from Persistence.interface_persistence import IPersistenceManager


class DataManager(IPersistenceManager):

    def __init__(self):
        self.storage = {}  # For the sake of simplicity, we'll use a dictionary as our storage

    def save(self, entity):
        entitytype = type(entity).__name__
        if entitytype not in self.storage:
            self.storage[entity_type] = {}
        self.storage[entity_type][entity.id] = entity

    def get(self, entity_id, entity_type):
        return self.storage.get(entity_type, {}).get(entity_id, None)

    def update(self, entity):
        entity_type = type(entity).__name__
        if entity_type in self.storage and entity.id in self.storage[entity_type]:
            self.storage[entity_type][entity.id] = entity

    def delete(self, entity_id, entity_type):
        if entity_type in self.storage and entity_id in self.storage[entity_type]:
            del self.storage[entity_type][entity_id]
