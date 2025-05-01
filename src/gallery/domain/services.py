from src.gallery.domain.entities import GalleryStore
from src.gallery.domain.repositories import IGalleryRepo
from src.shared.domain.exceptions import MissingValueException


class GalleryService:
    def __init__(self, gallery_repo: IGalleryRepo):
        self.gallery_repo = gallery_repo

    def validate_gallery(self, gallery: GalleryStore):
        self.__check_missing_fields(gallery)

    def __check_missing_fields(self, gallery: GalleryStore):
        if not gallery.src:
            raise MissingValueException(
                "Missing required fields: src")
