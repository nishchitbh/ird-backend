from src.auth.domain.entities.users_entity import UserOut
from src.gallery.domain.entities import GalleryStore, GalleryBase
from src.gallery.domain.repositories import IGalleryRepo, IScraper
from src.gallery.domain.services import GalleryService
from src.shared.domain.exceptions import (
    AuthenticationFailedException,
)


class GalleryUseCases:
    def __init__(self, gallery_repo: IGalleryRepo, gallery_service: GalleryService):
        self.gallery_repo = gallery_repo
        self.gallery_service = gallery_service

    def create_gallery(self, gallery: GalleryStore, user: UserOut):
        if user is None:
            raise AuthenticationFailedException("Unauthorized!")
        self.gallery_service.validate_gallery(gallery)
        return self.gallery_repo.create(GalleryStore(src=gallery.src, alt=gallery.alt, caption=gallery.caption, id=gallery.id))

    