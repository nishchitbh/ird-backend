from pymongo import MongoClient
from src.shared.config import SingletonMeta, setting


class Mongo(metaclass=SingletonMeta):
    def __init__(self):
        client = MongoClient(setting.mongodb_connection)
        self.db = client["IRDWebsite"]

    def get_db(self):
        return self.db


def get_db():
    db_instance = Mongo()
    return db_instance.get_db()
