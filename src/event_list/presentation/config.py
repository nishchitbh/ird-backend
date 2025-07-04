from src.event_list.infrastructure.event_list_repo_impl import EventListRepo
from src.event_list.application.event_use_cases import EventListUseCases
from src.shared.infrastructure.data_repo_impl import MongoRepo
from src.event_list.domain.services import EventListService
from src.shared.infrastructure.db_config import get_db
from fastapi import APIRouter

event_list_router = APIRouter(prefix="/event-lists", tags=["Event Lists"])


def get_event_list_cases():
    db = get_db()
    repo = MongoRepo(db=db, collection="flagship_programs")
    flagship_programs_repo = EventListRepo(repo=repo)
    flagship_services = EventListService(repo=flagship_programs_repo)
    return EventListUseCases(
        flagship_programs_repo=flagship_programs_repo,
        flagship_services=flagship_services,
    )
