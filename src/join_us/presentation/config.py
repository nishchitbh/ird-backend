from src.join_us.infrastructure.join_us_repo_impl import JoinUsRepoImpl
from src.join_us.application.join_us_use_cases import JoinUsUseCases
from src.shared.infrastructure.data_repo_impl import MongoRepo
from src.join_us.domain.services import JoinUsServices
from src.shared.infrastructure.db_config import get_db
from fastapi import APIRouter

join_us_router = APIRouter(prefix="/join-us", tags=["Join Us"])


def get_join_use_cases():
    db = get_db()
    repo = MongoRepo(db=db, collection="join_us")
    join_us_repo = JoinUsRepoImpl(repo=repo)
    join_services = JoinUsServices(repo=join_us_repo)
    return JoinUsUseCases(join_us_repo=join_us_repo, join_services=join_services)
