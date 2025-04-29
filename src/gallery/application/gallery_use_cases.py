from src.gallery.domain.entities import GalleryUpdate, GalleryUpload, GalleryStore
from src.auth.domain.entities.users_entity import UserOut
from src.gallery.domain.repositories import IGalleryRepo
from src.gallery.domain.services import GalleryService
from src.shared.domain.exceptions import (
    AuthenticationFailedException,
    ItemNotFoundException,
    ForbiddenException
)
from src.shared.config import setting
from fastapi import UploadFile
from bson import ObjectId
import uuid
import os


class GalleryUseCases:
    def __init__(self, gallery_repo: IGalleryRepo, gallery_service: GalleryService):
        self.gallery_repo = gallery_repo
        self.gallery_service = gallery_service

    def create_gallery(self, file: UploadFile, current_user: UserOut, gallery: GalleryUpload):
        if not current_user.approved:
            raise AuthenticationFailedException(
                "You cannot perform this action.")
        extension = os.path.splitext(file.filename)[1].lower()
        if extension not in setting.allowed_extensions:
            raise ForbiddenException("Invalid file type.")
        filename = f"{uuid.uuid4()}{extension}"
        os.makedirs(setting.upload_folder, exist_ok=True)
        file_path = os.path.join(setting.upload_folder, filename)
        with open(file_path, "wb") as buffer:
            buffer.write(file.file.read())
        src = f"{setting.upload_folder}/{filename}"
        gallery = GalleryStore(**gallery.model_dump(), src=src)
        self.gallery_service.validate_gallery(gallery)
        return self.gallery_repo.create(gallery.model_dump())

    def read_gallery(self, gallery_id: str):
        try:
            oid = ObjectId(gallery_id.strip())
        except Exception:
            raise ItemNotFoundException("Invalid gallery ID")

        gallery = self.gallery_repo.read(oid)
        if not gallery:
            raise ItemNotFoundException("Gallery not found.")

        return gallery

    def read_all(self):
        data = self.gallery_repo.read_all()
        return data

    def update_gallery(self, current_user: UserOut, gallery_id: str, gallery: GalleryUpdate):
        if not current_user.approved:
            raise AuthenticationFailedException(
                "You cannot perform this action.")
        gallery_id = gallery_id.strip()
        try:
            oid = ObjectId(gallery_id)
        except Exception:
            raise ItemNotFoundException("Invalid gallery ID")
        existing_gallery = self.gallery_repo.read(oid)
        if not existing_gallery:
            raise ItemNotFoundException("Gallery not found.")
        update_data = gallery.model_dump()
        update_data = {k: v for k, v in update_data.items() if v is not None}
        return self.gallery_repo.update(id=oid, update_data=update_data)

    def delete_gallery(self, current_user: UserOut, gallery_id: str):
        gallery_id = gallery_id.strip()
        try:
            oid = ObjectId(gallery_id)
        except Exception:
            raise ItemNotFoundException("Invalid gallery ID")
        if not current_user.approved:
            raise AuthenticationFailedException(
                "You cannot perform this action.")
        existing_gallery = self.gallery_repo.read(
            oid)
        if not existing_gallery:
            raise ItemNotFoundException("Gallery not found.")
        return self.gallery_repo.delete(oid)
