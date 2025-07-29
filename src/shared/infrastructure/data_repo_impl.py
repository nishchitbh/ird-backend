from pymongo.database import Database

from src.shared.domain.repositories.data_repo import IDataRepo


class MongoRepo(IDataRepo):
    def __init__(self, db: Database, collection: str):
        self.db = db
        self.collection = collection

    def create(self, data: dict) -> dict:
        result = self.db[self.collection].insert_one(data)
        data["_id"] = str(result.inserted_id)
        return data

    def read(self, identifier: dict) -> dict:
        result = self.db[self.collection].find_one(identifier)
        return result

    def update(self, identifier: dict, update_data: dict) -> dict:
        update_fields = {
            key: value for key, value in update_data.items() if value is not None
        }
        result = self.db[self.collection].find_one_and_update(
            identifier, {"$set": update_fields}, return_document=True
        )
        return result

    def delete(self, identifier: dict) -> dict:
        result = self.db[self.collection].delete_one(identifier)
        if result.deleted_count > 0:
            return {
                "status": "ok",
                "message": f"Data with identifier {identifier} deleted from collection {self.collection}.",
            }
        else:
            return None

    def read_all(self, page: int = 1, limit: int = 10) -> list:
        skip = (page - 1) * limit
        result = self.db[self.collection].find().skip(skip).limit(limit)
        return [doc for doc in result]
