from src.auth.domain.entities.users_entity import UserOut
from src.gallery.domain.entities import GalleryBase, GalleryUpdate
from src.gallery.domain.repositories import IGalleryRepo
from src.gallery.domain.services import GalleryService
from src.shared.domain.exceptions import (
    AuthenticationFailedException,
    ItemNotFoundException,
)
from bson import ObjectId


class GalleryUseCases:
    def __init__(self, gallery_repo: IGalleryRepo, gallery_service: GalleryService):
        self.gallery_repo = gallery_repo
        self.gallery_service = gallery_service

    def create_gallery(self, current_user: UserOut, gallery: GalleryBase, user: UserOut):
        self.gallery_service.validate_gallery(gallery)
        return self.gallery_repo.create(gallery)

    def read_gallery(self, gallery_id: str):
        return {"data": self.gallery_repo.read({"_id": ObjectId(gallery_id)})}

    def read_all(self):
        return {"data": self.gallery_repo.read_all()}

    def update_gallery(self, current_user: UserOut, gallery_id: str, gallery: GalleryUpdate):
        if not current_user.approved:
            raise AuthenticationFailedException("You cannot perform this action.")
        existing_gallery = self.gallery_repo.read({"_id": ObjectId(gallery_id)})
        if not existing_gallery:
            raise ItemNotFoundException("Gallery not found.")
        self.gallery_service.validate_gallery(gallery)
        update_data = gallery.model_dump()
        update_data = {k: v for k, v in update_data.items() if v is not None}
        return self.gallery_repo.update({"_id": ObjectId(gallery_id)}, update_data)
    
    