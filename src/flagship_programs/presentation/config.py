from src.flagship_programs.infrastructure.flagship_repo_impl import FlagshipRepo
from src.flagship_programs.application.flagship_use_cases import FlagshipUseCases
from src.shared.infrastructure.data_repo_impl import MongoRepo
from src.flagship_programs.domain.services import FlagshipService
from src.shared.infrastructure.db_config import get_db
from fastapi import APIRouter

flagship_programs_router = APIRouter(
    prefix="/flagship-programs", tags=["Flagship Programs"]
)


def get_flagship_programse_cases():
    db = get_db()
    repo = MongoRepo(db=db, collection="flagship_programs")
    flagship_programs_repo = FlagshipRepo(repo=repo)
    flagship_services = FlagshipService(repo=flagship_programs_repo)
    return FlagshipUseCases(
        flagship_programs_repo=flagship_programs_repo,
        flagship_services=flagship_services,
    )
