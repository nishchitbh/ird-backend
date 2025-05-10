from src.areas_of_work.infrastructure.areas_of_work_repo_impl import AreaRepoImpl
from src.areas_of_work.application.areas_of_work_use_cases import AreaUseCases
from src.shared.infrastructure.data_repo_impl import MongoRepo
from src.areas_of_work.domain.services import AreaServices
from src.shared.infrastructure.db_config import get_db
from fastapi import APIRouter

areas_router = APIRouter(prefix="/areas-of-work", tags=["Areas of Work"])


def get_areas_of_work_use_cases():
    db = get_db()
    repo = MongoRepo(db=db, collection="areas_of_work")
    area_repo = AreaRepoImpl(repo=repo)
    areas_services = AreaServices(area_repo=area_repo)
    return AreaUseCases(area_repo=area_repo, area_services=areas_services)
