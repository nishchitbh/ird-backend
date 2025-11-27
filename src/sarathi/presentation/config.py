# src/sarathi/presentation/config.py
from fastapi import APIRouter
from src.sarathi.infrastructure.repository import SarathiRepo
from src.sarathi.application.sarathi_service import SarathiAppService
from src.shared.infrastructure.db_config import get_db  

sarathi_router = APIRouter(prefix="/sarathi", tags=["Sarathi"])

from src.shared.infrastructure.data_repo_impl import MongoRepo
from src.shared.infrastructure.db_config import get_db


sarathi_router = APIRouter(prefix="/sarathi", tags=["Sarathi"])


def get_sarathi_use_cases():
    db = get_db()

    # Infrastructure Mongo repository
    mongo_repo = MongoRepo(db=db, collection="sarathi")

    # Infrastructure implementation of the domain interface
    infra_repo = SarathiRepo(repo=mongo_repo)

    # Application layer use cases
    return SarathiAppService(
        repo=infra_repo
    )