from pymongo.database import Database
from pymongo.errors import ConnectionFailure, OperationFailure, WriteError, InvalidOperation
from shared.domain.repositories.data_repo import DataRepo

class MongoRepo(DataRepo):
    def __init__(self, db: Database, collection: str):
        self.db = db
        self.collection = collection

    def handle_error(self, exception: Exception) -> dict:
        """Handles and returns a structured error message based on the exception."""
        if isinstance(exception, ConnectionFailure):
            return {
                "status": "error",
                "message": "Database connection failed."
            }
        elif isinstance(exception, WriteError):
            return {
                "status": "error",
                "message": f"Write operation failed: {exception.details}"
            }
        elif isinstance(exception, OperationFailure):
            return {
                "status": "error",
                "message": f"Operation failed: {exception.details}"
            }
        elif isinstance(exception, InvalidOperation):
            return {
                "status": "error",
                "message": f"Invalid operation: {exception.details}"
            }
        else:
            return {
                "status": "error",
                "message": str(exception)
            }

    def create(self, data: dict) -> dict:
        try:
            result = self.db[self.collection].insert_one(data)
            return {
                "status": "ok",
                "message": f"Data with id {result.inserted_id} created successfully on collection {self.collection}."
            }
        except Exception as e:
            return self.handle_error(e)

    def read(self, identifier: dict) -> dict:
        try:
            result = self.db[self.collection].find_one(identifier)
            if result:
                return {
                    "status": "ok",
                    "result": result
                }
            else:
                return {
                    "status": "failure",
                    "message": f"Data with identifier {identifier} not found on collection {self.collection}."}
        except Exception as e:
            return self.handle_error(e)

    def update(self, identifier: dict, update_data: dict) -> dict:
        try:
            result = self.db[self.collection].update_one(
                identifier,
                {"$set": update_data}
            )
            if result.modified_count > 0:
                return {
                    "status": "success",
                    "message": f"Data with identifier {identifier} updated successfully on collection {self.collection}."
                }
            else:
                return {
                    "status": "failure",
                    "message": f"No changes made or data with identifier {identifier} not found on collection {self.collection}."
                }

        except Exception as e:
            return self.handle_error(e)

    def delete(self, identifier: dict) -> dict:
        try:
            result = self.db[self.collection].delete_one(identifier)
            if result.deleted_count > 0:
                return {
                    "status": "ok",
                    "message": f"Data with identifier {identifier} deleted from collection {self.collection}."
                }
            else:
                return {
                    "status": "failure",
                    "message": f"Data with identifier {identifier} not found on collection {self.collection}."
                }
        except Exception as e:
            return self.handle_error(e)
