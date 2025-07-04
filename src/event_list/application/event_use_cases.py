from src.event_list.domain.entities import EventList, EventListUpdate
from src.shared.domain.exceptions import UnauthorizedException
from src.auth.domain.entities.users_entity import UserOut
from src.event_list.domain.repositories import IEventListRepo
from src.event_list.domain.services import EventListService


class EventListUseCases:
    def __init__(
        self, event_list_repo: IEventListRepo, event_list_services: EventListService
    ):
        self.repo = event_list_repo
        self.services = event_list_services

    def create_event_list(self, content: EventList, current_user: UserOut) -> EventList:
        if not current_user.approved:
            raise UnauthorizedException("You cannot perform this action.")
        self.services.verify_creation(content)
        return self.repo.create(content.model_dump())

    def update_event_list(
        self, id: str, content: EventListUpdate, current_user: UserOut
    ) -> EventList:
        if not current_user.approved:
            raise UnauthorizedException("You cannot perform this action.")
        update_data = content.model_dump()
        update_data = {k: v for k, v in update_data.items() if v is not None}
        message = self.repo.update(id, update_data)
        return message

    def delete_event_list(self, id: str, current_user: UserOut) -> dict:
        if not current_user.approved:
            raise UnauthorizedException("You cannot perform this action.")
        return self.repo.delete(id)

    def get_one_event(self, id: str) -> dict:
        return self.repo.read(id)

    def get_all_events(self) -> list:
        return self.repo.read_all()
