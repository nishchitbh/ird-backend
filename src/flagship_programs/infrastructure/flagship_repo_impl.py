from src.shared.domain.repositories.data_repo import IDataRepo
from src.shared.domain.exceptions import ItemNotFoundException
from src.flagship_programs.domain.repositories import IFlagshipRepo
from bson import ObjectId


class FlagshipRepo(IFlagshipRepo):
    def __init__(self, repo=IDataRepo):
        self.repo = repo

    def create(self, content: dict) -> dict:
        message = self.repo.create(content)
        return message

    def update(self, id: ObjectId, update_data: dict) -> dict:
        id = id.strip()
        try:
            oid = ObjectId(id)
        except Exception:
            raise ItemNotFoundException("Invalid ID")
        message = self.repo.update(
            {"_id": oid}, update_data)
        if not message:
            raise ItemNotFoundException(f"Item with id {id} not found")
        return message

    def read(self, id: str) -> dict:
        id = id.strip()
        try:
            oid = ObjectId(id)
        except Exception:
            raise ItemNotFoundException("Invalid ID")
        message = self.repo.read({"_id": oid})
        if message is None:
            raise ItemNotFoundException(f"Item with id {id} not found")
        return message

    def read_all(self) -> dict:
        message = self.repo.read_all()
        return message

    def delete(self, id: ObjectId) -> dict:
        id = id.strip()
        try:
            oid = ObjectId(id)
        except Exception:
            raise ItemNotFoundException("Invalid ID")
        message = self.repo.delete({"_id": oid})
        if not message:
            raise ItemNotFoundException(f"Item with id {id} not found")
        return message
