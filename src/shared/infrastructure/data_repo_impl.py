from pymongo.database import Database
from pymongo.errors import ConnectionFailure, OperationFailure, WriteError, InvalidOperation
from src.shared.domain.repositories.data_repo import IDataRepo
from src.shared.domain.exceptions import AppException, ItemNotFoundException
from fastapi import HTTPException


class MongoRepo(IDataRepo):
    def __init__(self, db: Database, collection: str):
        self.db = db
        self.collection = collection

    def handle_error(self, exception: Exception):
        """Handles and raises structured HTTP exceptions."""
        if isinstance(exception, ConnectionFailure):
            raise HTTPException(
                status_code=503, detail="Database connection failed.")
        elif isinstance(exception, WriteError):
            raise HTTPException(
                status_code=400, detail=f"Write operation failed: {exception.details}")
        elif isinstance(exception, OperationFailure):
            raise HTTPException(
                status_code=400, detail=f"Operation failed: {exception.details}")
        elif isinstance(exception, InvalidOperation):
            raise HTTPException(
                status_code=400, detail=f"Invalid operation: {exception.details}")
        elif isinstance(exception, AppException):
            raise exception
        else:
            raise HTTPException(status_code=500, detail=str(exception))

    def create(self, data: dict) -> dict:
        try:
            result = self.db[self.collection].insert_one(data)
            data["_id"] = str(result.inserted_id)
            return data
        except Exception as e:
            self.handle_error(e)

    def read(self, identifier: dict) -> dict:
        try:
            result = self.db[self.collection].find_one(identifier)
            if not result:
                raise ItemNotFoundException
            return result
        except Exception as e:
            self.handle_error(e)

    def update(self, identifier: dict, update_data: dict) -> dict:
        try:
            result = self.db[self.collection].find_one_and_update(
                identifier,
                {"$set": update_data},
                return_document=True 
            )
            return result

        except Exception as e:
            self.handle_error(e)

    def delete(self, identifier: dict) -> dict:
        try:
            result = self.db[self.collection].delete_one(identifier)
            if result.deleted_count > 0:
                return {
                    "status": "ok",
                    "message": f"Data with identifier {identifier} deleted from collection {self.collection}."
                }
            else:
                return None
        except Exception as e:
            self.handle_error(e)

    def read_all(self) -> list:
        try:
            result = self.db[self.collection].find()
            return [doc for doc in result]
        except Exception as e:
            self.handle_error(e)
