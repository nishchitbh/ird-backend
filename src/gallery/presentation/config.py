from src.gallery.infrastructure.gallery_repo_impl import GalleryRepoImpl
from src.gallery.application.gallery_use_cases import GalleryUseCases
from src.shared.infrastructure.data_repo_impl import MongoRepo
from src.gallery.domain.services import GalleryService
from src.shared.infrastructure.db_config import get_db
from fastapi import APIRouter

gallery_router = APIRouter(prefix="/gallery", tags=["Gallery"])


def get_gallery_use_cases():
    db = get_db()
    repo = MongoRepo(db=db, collection="gallery")
    gallery_repo = GalleryRepoImpl(repo=repo)
    gallery_services = GalleryService(gallery_repo=gallery_repo)
    return GalleryUseCases(gallery_repo=gallery_repo, gallery_service=gallery_services)
