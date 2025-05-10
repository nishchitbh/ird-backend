from src.gallery.domain.entities import GalleryUpdate, GalleryUpload, GalleryStore, GalleryOut
from src.auth.domain.entities.users_entity import UserOut
from src.gallery.domain.repositories import IGalleryRepo
from src.gallery.domain.services import GalleryService
from src.shared.domain.exceptions import (
    AuthenticationFailedException,
    ItemNotFoundException
)
from src.shared.utils import safe_join
from src.shared.config import setting
from fastapi import UploadFile
from bson import ObjectId
from pathlib import Path
import aiofiles
import uuid
import os


class GalleryUseCases:
    def __init__(self, gallery_repo: IGalleryRepo, gallery_service: GalleryService):
        self.gallery_repo = gallery_repo
        self.gallery_service = gallery_service

    async def create_gallery(self, file: UploadFile, current_user: UserOut, gallery: GalleryUpload):
        if not current_user.approved:
            raise AuthenticationFailedException(
                "You cannot perform this action.")

        await self.gallery_service.validate_picture(file)
        extension = os.path.splitext(file.filename)[1].lower()
        filename = f"{uuid.uuid4()}{extension}"
        target: Path = safe_join(setting.upload_folder, filename)
        contents = await file.read()
        async with aiofiles.open(target, "wb") as out_file:
            await out_file.write(contents)
        src = f"/uploads/{filename}"
        store = GalleryStore(**gallery.model_dump(), src=src)
        self.gallery_service.validate_gallery(store)

        record = self.gallery_repo.create(store.model_dump())
        return GalleryOut.model_validate(record)

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
        if not current_user.approved:
            raise AuthenticationFailedException(
                "You cannot perform this action.")
        gallery_id = gallery_id.strip()
        try:
            oid = ObjectId(gallery_id)
        except Exception:
            raise ItemNotFoundException("Invalid gallery ID")
        existing_gallery = self.gallery_repo.read(
            oid)
        if not existing_gallery:
            raise ItemNotFoundException("Gallery not found.")
        gallery = self.gallery_repo.read(oid)
        self.gallery_service.delete_image(gallery["src"])
        return self.gallery_repo.delete(oid)

    def read_gallery(self, gallery_id: str):
        gallery_id = gallery_id.strip()
        try:
            oid = ObjectId(gallery_id)
        except Exception:
            raise ItemNotFoundException("Invalid gallery ID")
        gallery = self.gallery_repo.read(oid)
        if not gallery:
            raise ItemNotFoundException("Gallery not found.")
        return gallery

    def read_all(self):
        return self.gallery_repo.read_all()
