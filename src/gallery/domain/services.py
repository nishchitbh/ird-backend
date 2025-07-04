import os
from fastapi import UploadFile
from src.shared.config import setting
from src.gallery.domain.entities import GalleryStore
from src.gallery.domain.repositories import IGalleryRepo
from src.shared.domain.exceptions import (
    MissingValueException,
    ForbiddenException,
    RequestEntityTooLargeException,
)


class GalleryService:
    def __init__(self, gallery_repo: IGalleryRepo):
        self.gallery_repo = gallery_repo

    def validate_gallery(self, gallery: GalleryStore):
        self.__check_missing_fields(gallery)

    async def validate_picture(self, picture: UploadFile):
        self.__check_filetype(picture)
        await self.__check_filesize(picture)
        await picture.seek(0)

    def __check_filetype(self, file: UploadFile):
        extension = os.path.splitext(file.filename)[1].lower()
        if extension not in setting.allowed_extensions:
            raise ForbiddenException("Invalid file type for picture.")

    async def __check_filesize(self, file: UploadFile):
        total = 0
        while True:
            chunk = await file.read(setting.chunk_size)
            if not chunk:
                break
            total += len(chunk)
            if total > setting.max_file_size:
                raise RequestEntityTooLargeException("File too large.")

    def __check_missing_fields(self, gallery: GalleryStore):
        if not gallery.src:
            raise MissingValueException("Missing required fields: src")

    def delete_image(self, src: str):
        os.remove(src)
