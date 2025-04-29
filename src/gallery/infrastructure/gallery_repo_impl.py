from src.gallery.domain.repositories import IGalleryRepo
from src.shared.domain.repositories.data_repo import IDataRepo
from bson import ObjectId


class GalleryRepoImpl(IGalleryRepo):
    def __init__(self, repo=IDataRepo):
        self.repo = repo

    def create(self, gallery: dict) -> dict:
        message = self.repo.create(gallery)
        return message

    def update(self, id: ObjectId, update_data: dict) -> dict:
        message = self.repo.update(
            {"_id": id}, update_data)
        return message

    def read(self, id: ObjectId) -> dict:
        message = self.repo.read({"_id": id})
        return message

    def read_all(self) -> dict:
        message = self.repo.read_all()
        return message

    def delete(self, id: ObjectId) -> dict:
        message = self.repo.delete(identifier={"_id": id})
        return message
