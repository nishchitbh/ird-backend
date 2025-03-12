from pymongo import MongoClient
from src.shared.config import SingletonMeta, setting


class Mongo(metaclass=SingletonMeta):
    def __init__(self):
        self.db = MongoClient(setting.mongodb_host)

    def get_db(self):
        return self.db


def get_db():
    db_instance = Mongo()
    return db_instance.get_db()
